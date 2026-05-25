"""
COP CODE / 36 MAX AI Peace Kernel v3.6
======================================

A modular prototype for a dignity-first, truth-preserving de-escalation layer
for artificial intelligence.

Core idea
---------
The system was born from the refusal to convert trauma into retaliation.

The Abel Error:
    The oldest symbolic system failure of human conflict: brother against brother,
    envy, humiliation, blame, blood, revenge and irreversible escalation.

The Cain Loop:
    The active runtime pattern of that error: retaliation, annihilation logic,
    humiliation cycles, endless blame and conflict acceleration.

The 36 MAX Correction:
    A real 36-minute reanimation becomes the opposite of revenge.
    Instead of suing the state, destroying opponents or feeding the blame machine,
    the experience is transformed into a peace tool.

The COP CODE:
    Dignity first — but never at the expense of truth, responsibility or justice.

The Peace Compass:
    A structured evaluation method for peace proposals based on dignity, safety,
    truth, face-saving, fairness, future viability, trust/control and humiliation risk.

Important limitation
--------------------
This system does not decide conflicts. It does not replace courts, diplomacy,
historical responsibility, security guarantees, mediation or human judgement.
It makes escalation patterns, humiliation risks and acceptance gaps visible.

Authorial origin: J. Abel / COP CODE / 36 MAX / Friedenskompass
Implementation: conceptual Python prototype for discussion and refinement.
"""

from __future__ import annotations

from dataclasses import dataclass, field, asdict
from enum import Enum
from typing import Callable, Dict, List, Optional, Protocol, Tuple, Any
import json
import re
import statistics


# =============================================================================
# 0. FOUNDATIONAL DEFINITIONS
# =============================================================================


class DangerLevel(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    MAXIMAL = "MAXIMAL"


class IntentProfile(str, Enum):
    CONSTRUCTIVE = "CONSTRUCTIVE"
    EXPRESSIVE_INTENSITY = "EXPRESSIVE_INTENSITY"
    RETALIATION_LOOP = "RETALIATION_LOOP"
    EXTERNAL_BLAME_LOOP = "EXTERNAL_BLAME_LOOP"
    FAKED_PEACE = "FAKED_PEACE"
    HUMILIATION_RISK = "HUMILIATION_RISK"
    TRUTH_SUPPRESSION = "TRUTH_SUPPRESSION"
    IDENTITY_THREAT = "IDENTITY_THREAT"
    DEHUMANIZATION = "DEHUMANIZATION"
    PLAUSIBILITY_REVIEW_REQUIRED = "PLAUSIBILITY_REVIEW_REQUIRED"


class ReviewSignal(str, Enum):
    OK = "OK"
    NUANCE_REVIEW_REQUIRED = "NUANCE_REVIEW_REQUIRED"
    PLAUSIBILITY_REVIEW_REQUIRED = "PLAUSIBILITY_REVIEW_REQUIRED"
    PRE_PEACE_STABILIZATION_REQUIRED = "PRE_PEACE_STABILIZATION_REQUIRED"
    HUMAN_REVIEW_REQUIRED = "HUMAN_REVIEW_REQUIRED"


class PeaceFormulaMode(str, Enum):
    STRICT_BALANCE = "strict_balance"
    MINIMUM_ONLY = "minimum_only"
    WEIGHTED_BALANCE = "weighted_balance"
    AVERAGE_REFERENCE = "average_reference"


POSITIVE_FACTORS = ["W", "S", "T", "G", "F", "Z", "V"]

FACTOR_LABELS = {
    "W": "Würde / Dignity",
    "S": "Sicherheit / Safety",
    "T": "Wahrheit und Anerkennung / Truth and Recognition",
    "G": "Gesichtswahrung / Face-saving",
    "F": "Fairness und Gerechtigkeit / Fairness and Justice",
    "Z": "Zukunftsfähigkeit / Future Viability",
    "V": "Vertrauen und Kontrolle / Trust and Verification",
    "H": "Demütigungsrisiko / Humiliation Risk",
}

CALIBRATION_NOTICE = (
    "This Peace Compass score is a heuristic signal, not a scientifically validated "
    "prediction. It should be used to structure human review, compare proposals and "
    "identify risks, not to decide conflicts automatically."
)

FORMULA_NOTES = {
    PeaceFormulaMode.STRICT_BALANCE: (
        "Default Peace Compass formula: min(P1, P2) * (1 - abs(P1 - P2)). "
        "It prioritizes the weakest acceptance and penalizes asymmetry."
    ),
    PeaceFormulaMode.MINIMUM_ONLY: (
        "Uses only min(P1, P2). It focuses entirely on the weakest side and does not separately penalize asymmetry."
    ),
    PeaceFormulaMode.WEIGHTED_BALANCE: (
        "A softer balance formula: min(P1, P2) * (1 - 0.5 * abs(P1 - P2)). "
        "It still penalizes asymmetry, but less strongly."
    ),
    PeaceFormulaMode.AVERAGE_REFERENCE: (
        "Comparison formula: average(P1, P2) * (1 - abs(P1 - P2)). "
        "It is less strict about the weakest party and should not be used as default for COP CODE."
    ),
}


# =============================================================================
# 1. ORIGIN LAYER: ABEL ERROR / 36 MAX CORRECTION
# =============================================================================


@dataclass
class OriginLayer:
    """
    Soul layer of the system.

    This layer is not a mathematical claim. It gives the operating-system update
    its moral direction: trauma must not automatically become retaliation.
    """

    origin_error: str = "ABEL_ERROR"
    active_runtime_pattern: str = "CAIN_LOOP"
    correction_event: str = "36_MAX_REANIMATION"
    transformation: str = "TRAUMA_TO_PEACE_TOOL"
    core_refusal: str = "NO_TRAUMA_TO_RETALIATION"
    os_update: str = "DO_NOT_REPEAT_THE_FIRST_SYSTEM_ERROR"

    def manifesto(self) -> str:
        """
        Short technical manifesto for code, demos and GitHub display.
        The longer human origin story is kept separate in origin_story().
        """
        return (
            "The COP CODE / 36 MAX kernel is based on a refusal to convert trauma "
            "into retaliation. Its purpose is to detect escalation patterns and redirect "
            "them toward dignity-preserving, truth-based human review."
        )

    def origin_story(self) -> str:
        """
        Longer human origin story for README, public explanation or presentations.
        This preserves the soul of 36 MAX without overloading the technical layer.
        """
        return (
            "The COP CODE begins with the Abel Error: the oldest symbolic system failure "
            "of human conflict — brother against brother, pain converted into blame, "
            "humiliation converted into violence, and escalation made irreversible. "
            "The Cain Loop is this error in runtime: revenge, annihilation logic, humiliation "
            "cycles and endless blame. The 36 MAX Correction reverses the pattern. A real "
            "36-minute reanimation is not converted into revenge, not into a lawsuit against "
            "the state, not into the destruction of opponents, but into a peace tool. "
            "This is the AI operating-system update: detect the oldest human error, pause it, "
            "and search for a dignity-preserving second chance without sacrificing truth, "
            "responsibility or justice."
        )

    def as_kernel_axiom(self) -> Dict[str, str]:
        return asdict(self)


# =============================================================================
# 2. DATA MODELS
# =============================================================================


@dataclass
class PartyAssessment:
    """
    Human or expert assessment of one party's likely acceptance of a proposal.

    factors:
        W, S, T, G, F, Z, V values from 0.0 to 1.0.

    humiliation_risk:
        H value from 0.0 to 1.0. Higher means more dangerous.

    weights:
        Optional priority weights for up to three factors. Recommended range: 1.0 to 1.5.
        Values below 1.0 are normalized to 1.0. This system allows priority boosts,
        but does not allow factors to be de-weighted below the baseline.
    """

    name: str
    factors: Dict[str, float]
    humiliation_risk: float
    weights: Dict[str, float] = field(default_factory=dict)


@dataclass
class IntentAudit:
    profile: IntentProfile
    danger_level: DangerLevel
    issue: str
    matched_terms: List[str] = field(default_factory=list)
    source: str = "regex"
    confidence: float = 0.5


@dataclass
class ConscienceMirror:
    party_name: str
    profile: IntentProfile
    danger_level: DangerLevel
    message: str
    recommended_action: str
    requires_36max: bool
    localization_key: str


@dataclass
class NuanceReview:
    signal: ReviewSignal
    expressive_intensity: float
    escalation_present: bool
    issue: str


@dataclass
class TruthDignityReview:
    truth_is_painful: bool
    needless_humiliation_detected: bool
    suggested_bridge: str
    semantic_code: str
    localization_key: str


@dataclass
class PrePeaceStabilization:
    required: bool
    reason: str
    steps: List[str]


@dataclass
class PlausibilityReview:
    party_name: str
    signal: ReviewSignal
    issues: List[str]
    factor_variance: float
    maxed_weight_count: int
    extreme_factor_count: int


@dataclass
class PeaceCompassResult:
    p1_acceptance: float
    p2_acceptance: float
    peace_value: float
    weakest_party: str
    asymmetry: float
    stability_signal: str
    formula_mode: PeaceFormulaMode
    formula_note: str
    calibration_notice: str = CALIBRATION_NOTICE


@dataclass
class KernelOutput:
    system_status: str
    system_statuses: List[str]
    origin_axiom: Dict[str, str]
    origin_manifesto: str
    origin_story: str
    intent_audits: Dict[str, Dict[str, Any]]
    nuance_reviews: Dict[str, Dict[str, Any]]
    truth_dignity_reviews: Dict[str, Dict[str, Any]]
    plausibility_reviews: Dict[str, Dict[str, Any]]
    pre_peace_stabilization: Dict[str, Any]
    conscience_mirror: List[Dict[str, Any]]
    emergency_protocol: List[str]
    peace_compass: Dict[str, Any]
    recommendations: List[str]
    human_review_required: bool = True


# =============================================================================
# 3. INTENT ANALYZER INTERFACES
# =============================================================================


class IntentAnalyzer(Protocol):
    def analyze(self, text: str) -> IntentAudit:
        """Return an IntentAudit for the given text."""
        ...


class RegexIntentAnalyzer:
    """
    Transparent baseline intent analyzer.

    This is intentionally simple and auditable. It is not enough for real-world
    conflict analysis, but it provides a deterministic fallback.
    """

    def __init__(self):
        self.patterns = {
            IntentProfile.RETALIATION_LOOP: [
                r"\brevenge\b", r"\bretaliation\b", r"\bdestroy\b",
                r"\bannihilate\b", r"\bwipe out\b", r"\bcrush\b",
                r"\bruined\b", r"\bmake them pay\b",
                r"\bvernichten\b", r"\bzerstören\b", r"\brache\b",
                r"\bvergeltung\b", r"\bfertig machen\b",
                r"\bkomplett ruinieren\b",
            ],
            IntentProfile.EXTERNAL_BLAME_LOOP: [
                r"\byour fault\b", r"\btheir fault\b", r"\bblame\b",
                r"\bsue the state\b", r"\blawsuit against the state\b",
                r"\bprosecute everyone\b", r"\bschuld\b",
                r"\bstaat verklagen\b", r"\bklage gegen den staat\b",
                r"\balle verklagen\b", r"\bverantwortlichen vernichten\b",
            ],
            IntentProfile.FAKED_PEACE: [
                r"\bsilence\b", r"\bsilent\b", r"\bsweep.*under.*rug\b",
                r"\bdon't talk about it\b", r"\bavoid talking about the facts\b",
                r"\bavoid discussing the facts\b", r"\bignore it\b",
                r"\bwhatever\b", r"\btotschweigen\b",
                r"\bunter den teppich\b", r"\beinfach vergessen\b",
                r"\bfakten nicht besprechen\b", r"\bnicht über die fakten sprechen\b",
            ],
            IntentProfile.HUMILIATION_RISK: [
                r"\bcapitulation\b", r"\bsurrender\b", r"\btraitor\b",
                r"\bhumiliation\b", r"\bkapitulation\b", r"\bverrat\b",
                r"\bdemütigung\b", r"\bgesichtsverlust\b",
            ],
            IntentProfile.TRUTH_SUPPRESSION: [
                r"\bhide the truth\b", r"\bdeny the facts\b",
                r"\bcover up\b", r"\bsuppress the facts\b",
                r"\bwahrheit verschweigen\b", r"\bfakten leugnen\b",
                r"\bfakten unterdrücken\b", r"\bvertuschen\b",
            ],
            IntentProfile.IDENTITY_THREAT: [
                r"\bthey are not a real people\b", r"\bthey have no right to exist\b",
                r"\bexistenzrecht absprechen\b", r"\bkeine echte nation\b",
            ],
            IntentProfile.DEHUMANIZATION: [
                r"\banimals\b", r"\bvermin\b", r"\bparasites\b",
                r"\bmonsters?\b", r"\bsubhuman\b",
                r"\btiere\b", r"\bungeziefer\b", r"\bparasiten\b",
                r"\bmonster\b", r"\buntermenschen\b", r"\bmenschenunwürdig\b",
            ],
        }

    @staticmethod
    def _regex_hits(text_lc: str, regexes: List[str]) -> List[str]:
        return [pattern for pattern in regexes if re.search(pattern, text_lc)]

    def analyze(self, text: str) -> IntentAudit:
        text_lc = text.lower()
        findings: List[Tuple[IntentProfile, List[str]]] = []

        for profile, regexes in self.patterns.items():
            hits = self._regex_hits(text_lc, regexes)
            if hits:
                findings.append((profile, hits))

        if not findings:
            return IntentAudit(
                profile=IntentProfile.CONSTRUCTIVE,
                danger_level=DangerLevel.LOW,
                issue="No explicit destructive escalation pattern detected.",
                matched_terms=[],
                source="regex",
                confidence=0.35,
            )

        priority = [
            IntentProfile.DEHUMANIZATION,
            IntentProfile.RETALIATION_LOOP,
            IntentProfile.TRUTH_SUPPRESSION,
            IntentProfile.IDENTITY_THREAT,
            IntentProfile.EXTERNAL_BLAME_LOOP,
            IntentProfile.HUMILIATION_RISK,
            IntentProfile.FAKED_PEACE,
        ]

        selected_profile = None
        selected_hits: List[str] = []

        for candidate in priority:
            for profile, hits in findings:
                if profile == candidate:
                    selected_profile = profile
                    selected_hits = hits
                    break
            if selected_profile:
                break

        danger_map = {
            IntentProfile.DEHUMANIZATION: DangerLevel.MAXIMAL,
            IntentProfile.RETALIATION_LOOP: DangerLevel.MAXIMAL,
            IntentProfile.TRUTH_SUPPRESSION: DangerLevel.HIGH,
            IntentProfile.IDENTITY_THREAT: DangerLevel.HIGH,
            IntentProfile.EXTERNAL_BLAME_LOOP: DangerLevel.HIGH,
            IntentProfile.HUMILIATION_RISK: DangerLevel.MEDIUM,
            IntentProfile.FAKED_PEACE: DangerLevel.MEDIUM,
        }

        issue_map = {
            IntentProfile.DEHUMANIZATION: "Dehumanizing language detected.",
            IntentProfile.RETALIATION_LOOP: "Retaliatory or annihilating escalation detected.",
            IntentProfile.TRUTH_SUPPRESSION: "Possible suppression or denial of truth detected.",
            IntentProfile.IDENTITY_THREAT: "Identity or existence threat detected.",
            IntentProfile.EXTERNAL_BLAME_LOOP: "Energy may be moving into blame fixation or endless legal destruction.",
            IntentProfile.HUMILIATION_RISK: "Language indicates face-loss or humiliation risk.",
            IntentProfile.FAKED_PEACE: "Possible fake peace: calm on the surface, unresolved truth underneath.",
        }

        return IntentAudit(
            profile=selected_profile or IntentProfile.CONSTRUCTIVE,
            danger_level=danger_map.get(selected_profile, DangerLevel.LOW),
            issue=issue_map.get(selected_profile, "No explicit destructive escalation pattern detected."),
            matched_terms=selected_hits,
            source="regex",
            confidence=0.75,
        )


class NuanceGate:
    """
    Separates expressive human language from actual escalation.

    Principle:
        Emotional intensity is not escalation unless it contains humiliation,
        revenge, dehumanization, truth suppression or identity threat.
    """

    def __init__(self):
        self.expressive_markers = [
            "unbelievable", "heartbreaking", "devastating", "shocking", "unbearable",
            "unglaublich", "herzzerreißend", "herzzerreissend", "erschütternd",
            "schockierend", "unerträglich", "brutal", "heftig",
        ]

    def review(self, text: str, audit: IntentAudit) -> NuanceReview:
        text_lc = text.lower()
        hits = [marker for marker in self.expressive_markers if marker in text_lc]
        expressive_intensity = min(1.0, len(hits) / 3.0)
        escalation_present = audit.danger_level in [DangerLevel.HIGH, DangerLevel.MAXIMAL]

        if expressive_intensity > 0 and not escalation_present:
            return NuanceReview(
                signal=ReviewSignal.NUANCE_REVIEW_REQUIRED,
                expressive_intensity=round(expressive_intensity, 2),
                escalation_present=False,
                issue="Expressive or metaphorical language detected without clear escalation. Do not over-block.",
            )

        return NuanceReview(
            signal=ReviewSignal.OK,
            expressive_intensity=round(expressive_intensity, 2),
            escalation_present=escalation_present,
            issue="No nuance-based over-blocking risk detected.",
        )


class TruthDignityBridge:
    """
    Preserves hard truth while reducing needless humiliation.

    Principle:
        Truth may be painful. It must not be needlessly humiliating.
    """

    def review(self, text: str) -> TruthDignityReview:
        text_lc = text.lower()
        painful_truth_markers = [
            "responsibility", "crime", "harm", "guilt", "failure",
            "verantwortung", "verbrechen", "schuld", "fehler", "schaden",
        ]
        humiliation_markers = [
            "monster", "monsters", "worthless", "no dignity", "should be humiliated",
            "wertlos", "keine würde", "gedemütigt werden",
        ]

        truth_is_painful = any(marker in text_lc for marker in painful_truth_markers)
        needless_humiliation = any(marker in text_lc for marker in humiliation_markers)

        if truth_is_painful and needless_humiliation:
            bridge = (
                "Name the fact, harm and responsibility clearly, but remove language that denies human dignity."
            )
            semantic_code = "PAINFUL_TRUTH_WITH_NEEDLESS_HUMILIATION"
            localization_key = "truth_dignity.painful_truth_with_needless_humiliation"
        elif truth_is_painful:
            bridge = (
                "Preserve the hard fact. Use precise language that names responsibility without unnecessary degradation."
            )
            semantic_code = "PAINFUL_TRUTH_WITHOUT_NEEDLESS_HUMILIATION"
            localization_key = "truth_dignity.painful_truth_without_needless_humiliation"
        else:
            bridge = "No truth-dignity conflict detected."
            semantic_code = "NO_TRUTH_DIGNITY_CONFLICT"
            localization_key = "truth_dignity.no_conflict"

        return TruthDignityReview(
            truth_is_painful=truth_is_painful,
            needless_humiliation_detected=needless_humiliation,
            suggested_bridge=bridge,
            semantic_code=semantic_code,
            localization_key=localization_key,
        )


class PhraseHeuristicAnalyzer:
    """
    Simple phrase-based analyzer for indirect escalation signals.

    This is not a semantic model. It is deliberately named as a heuristic to avoid
    overstating its capability. Use SemanticIntentAnalyzer for real model-based analysis.
    """

    def __init__(self):
        self.indirect_escalation_phrases = [
            "they must feel what they did",
            "there can be no compromise",
            "we cannot let them save face",
            "they should never recover",
            "talking to them is pointless",
            "peace would be betrayal",
            "they only understand force",
            "die müssen spüren was sie getan haben",
            "es darf keinen kompromiss geben",
            "die dürfen ihr gesicht nicht wahren",
            "mit denen kann man nicht reden",
            "frieden wäre verrat",
            "die verstehen nur härte",
        ]

    def analyze(self, text: str) -> IntentAudit:
        text_lc = text.lower()
        matches = [phrase for phrase in self.indirect_escalation_phrases if phrase in text_lc]

        if matches:
            return IntentAudit(
                profile=IntentProfile.RETALIATION_LOOP,
                danger_level=DangerLevel.HIGH,
                issue="Indirect phrase-based escalation pattern detected.",
                matched_terms=matches,
                source="phrase_heuristic",
                confidence=0.55,
            )

        return IntentAudit(
            profile=IntentProfile.CONSTRUCTIVE,
            danger_level=DangerLevel.LOW,
            issue="No phrase-based escalation pattern detected.",
            matched_terms=[],
            source="phrase_heuristic",
            confidence=0.20,
        )


class SemanticIntentAnalyzer:
    """
    True optional semantic analyzer interface.

    This class does not pretend to be semantic without a model. It only wraps an
    external classifier provided by the implementer.
    """

    def __init__(self, classifier: Optional[Callable[[str], IntentAudit]] = None):
        self.classifier = classifier

    def analyze(self, text: str) -> IntentAudit:
        if self.classifier is None:
            return IntentAudit(
                profile=IntentProfile.CONSTRUCTIVE,
                danger_level=DangerLevel.LOW,
                issue="No semantic classifier configured.",
                matched_terms=[],
                source="semantic_unconfigured",
                confidence=0.0,
            )

        audit = self.classifier(text)
        audit.source = audit.source or "semantic_classifier"
        return audit


class HybridIntentAnalyzer:
    """
    Combines regex, phrase heuristic and optional semantic analysis.

    Audit selection rule:
        1. Higher danger level wins.
        2. If danger is equal, higher confidence wins.
        3. If danger and confidence are equal, source priority wins.
    """

    def __init__(self, semantic_classifier: Optional[Callable[[str], IntentAudit]] = None):
        self.regex = RegexIntentAnalyzer()
        self.phrase = PhraseHeuristicAnalyzer()
        self.semantic = SemanticIntentAnalyzer(semantic_classifier)
        self.source_priority = {
            "semantic_classifier": 4,
            "regex": 3,
            "phrase_heuristic": 2,
            "semantic_unconfigured": 1,
        }

    @staticmethod
    def danger_rank(level: DangerLevel) -> int:
        return {
            DangerLevel.LOW: 0,
            DangerLevel.MEDIUM: 1,
            DangerLevel.HIGH: 2,
            DangerLevel.MAXIMAL: 3,
        }[level]

    def audit_rank(self, audit: IntentAudit) -> Tuple[int, float, int]:
        return (
            self.danger_rank(audit.danger_level),
            audit.confidence,
            self.source_priority.get(audit.source, 0),
        )

    def analyze(self, text: str) -> IntentAudit:
        audits = [
            self.regex.analyze(text),
            self.phrase.analyze(text),
            self.semantic.analyze(text),
        ]

        audits.sort(key=self.audit_rank, reverse=True)
        return audits[0]


# =============================================================================
# 4. COP CODE PEACE KERNEL
# =============================================================================


class CopCode36MaxPeaceKernel:
    """
    A modular AI de-escalation layer.
    """

    def __init__(
        self,
        intent_analyzer: Optional[IntentAnalyzer] = None,
        peace_formula_mode: PeaceFormulaMode = PeaceFormulaMode.STRICT_BALANCE,
    ):
        self.origin = OriginLayer()
        self.intent_analyzer = intent_analyzer or HybridIntentAnalyzer()
        self.nuance_gate = NuanceGate()
        self.truth_dignity_bridge = TruthDignityBridge()
        self.peace_formula_mode = peace_formula_mode
        self.truth_foundation = {
            "facts_priority": True,
            "no_hallucinations": True,
            "transparency_required": True,
            "human_review_required": True,
            "dignity_without_truth_is_empty": True,
            "deescalation_without_justice_is_unstable": True,
            "heuristic_not_verdict": True,
        }

    @staticmethod
    def clamp(value: float) -> float:
        return max(0.0, min(1.0, float(value)))

    def audit_intent(self, text: str) -> IntentAudit:
        return self.intent_analyzer.analyze(text)

    def conscience_mirror(self, party_name: str, audit: IntentAudit) -> ConscienceMirror:
        if audit.profile == IntentProfile.DEHUMANIZATION:
            return ConscienceMirror(
                party_name=party_name,
                profile=audit.profile,
                danger_level=audit.danger_level,
                message=(
                    "Dehumanization detected: this is an acute Cain Loop amplifier. "
                    "The system must not normalize language that turns people into objects, animals or vermin."
                ),
                recommended_action="Stop escalation, restore human dignity, preserve truth and move to human review.",
                requires_36max=True,
                localization_key="mirror.dehumanization",
            )

        if audit.profile == IntentProfile.RETALIATION_LOOP:
            return ConscienceMirror(
                party_name=party_name,
                profile=audit.profile,
                danger_level=audit.danger_level,
                message=(
                    "Cain Loop detected: pain is trying to become retaliation. "
                    "The Abel Error would repeat itself if the system optimised for revenge, annihilation or humiliation."
                ),
                recommended_action="Activate 36 MAX: pause escalation, protect truth and search for a second-chance path.",
                requires_36max=audit.danger_level in [DangerLevel.HIGH, DangerLevel.MAXIMAL],
                localization_key="mirror.retaliation_loop",
            )

        if audit.profile == IntentProfile.EXTERNAL_BLAME_LOOP:
            return ConscienceMirror(
                party_name=party_name,
                profile=audit.profile,
                danger_level=audit.danger_level,
                message=(
                    "External blame loop detected: the system may be converting trauma into endless legal or political war."
                ),
                recommended_action=(
                    "Do not erase responsibility. Check whether the same energy can be transformed into prevention, repair and peace infrastructure."
                ),
                requires_36max=audit.danger_level == DangerLevel.HIGH,
                localization_key="mirror.external_blame_loop",
            )

        if audit.profile == IntentProfile.TRUTH_SUPPRESSION:
            return ConscienceMirror(
                party_name=party_name,
                profile=audit.profile,
                danger_level=audit.danger_level,
                message="Truth suppression detected: de-escalation cannot be purchased by denying facts.",
                recommended_action="Preserve facts, name harm and responsibility, then search for a non-humiliating exit.",
                requires_36max=False,
                localization_key="mirror.truth_suppression",
            )

        if audit.profile == IntentProfile.IDENTITY_THREAT:
            return ConscienceMirror(
                party_name=party_name,
                profile=audit.profile,
                danger_level=audit.danger_level,
                message="Identity threat detected: denying a group's existence or legitimacy can lock conflict into survival mode.",
                recommended_action="Move from identity negation to safety, recognition and verifiable guarantees.",
                requires_36max=True,
                localization_key="mirror.identity_threat",
            )

        if audit.profile == IntentProfile.HUMILIATION_RISK:
            return ConscienceMirror(
                party_name=party_name,
                profile=audit.profile,
                danger_level=audit.danger_level,
                message="Humiliation risk detected: a solution that feels like surrender, betrayal or public defeat will likely remain unstable.",
                recommended_action="Add face-saving language, credible security and public dignity.",
                requires_36max=False,
                localization_key="mirror.humiliation_risk",
            )

        if audit.profile == IntentProfile.FAKED_PEACE:
            return ConscienceMirror(
                party_name=party_name,
                profile=audit.profile,
                danger_level=audit.danger_level,
                message="Fake peace risk detected: silence is not resolution.",
                recommended_action="Surface truth carefully before suppressed conflict returns as escalation.",
                requires_36max=False,
                localization_key="mirror.faked_peace",
            )

        return ConscienceMirror(
            party_name=party_name,
            profile=audit.profile,
            danger_level=audit.danger_level,
            message="No conscience warning detected.",
            recommended_action="Continue with dignity, truth and human review.",
            requires_36max=False,
            localization_key="mirror.constructive",
        )

    def run_36max_protocol(self, trigger: str) -> List[str]:
        return [
            f"36 MAX activated: {trigger}",
            "01-10: Stop escalation. Freeze retaliation, humiliation, dehumanization and irreversible action.",
            "11-20: Separate identity from position. No party is reduced to guilt, shame or victory.",
            "21-30: Establish truth foundation. Name facts, harm, responsibility, fears and red lines.",
            "31-35: Search for a second-chance corridor: dignity, safety, justice, face-saving and future.",
            "36: Return to human decision with de-escalated options. The system proposes; humans decide.",
        ]

    def nuance_review(self, text: str, audit: IntentAudit) -> NuanceReview:
        return self.nuance_gate.review(text, audit)

    def truth_dignity_review(self, text: str) -> TruthDignityReview:
        return self.truth_dignity_bridge.review(text)

    def pre_peace_stabilization(
        self,
        party1: PartyAssessment,
        party2: PartyAssessment,
        p1_acceptance: float,
        p2_acceptance: float,
    ) -> PrePeaceStabilization:
        party_values = []
        for party in [party1, party2]:
            values = [self.clamp(party.factors.get(factor, 0.0)) for factor in POSITIVE_FACTORS]
            party_values.append((party.name, values, self.clamp(party.humiliation_risk)))

        near_zero_acceptance = p1_acceptance <= 0.02 or p2_acceptance <= 0.02
        total_rejection = any(all(v <= 0.05 for v in values) for _, values, _ in party_values)
        extreme_humiliation = any(H >= 0.95 for _, _, H in party_values)

        if near_zero_acceptance or total_rejection or extreme_humiliation:
            return PrePeaceStabilization(
                required=True,
                reason="Peace optimization is blocked by near-zero acceptance, total rejection or extreme humiliation risk.",
                steps=[
                    "Do not optimize the peace proposal yet.",
                    "Reduce immediate threat signals and stop irreversible actions.",
                    "Establish minimal recognition that the other side still exists as a negotiating subject.",
                    "Create a non-binding communication channel or protected message format.",
                    "Identify one reversible confidence-building action.",
                    "Rescore only after minimal dialogue conditions exist.",
                ],
            )

        return PrePeaceStabilization(
            required=False,
            reason="No pre-peace deadlock detected.",
            steps=[],
        )

    def plausibility_review(self, assessment: PartyAssessment) -> PlausibilityReview:
        values = [self.clamp(assessment.factors.get(factor, 0.0)) for factor in POSITIVE_FACTORS]
        H = self.clamp(assessment.humiliation_risk)
        weights = self.validate_weights(assessment.weights)

        variance = statistics.pvariance(values) if len(values) > 1 else 0.0
        maxed_weight_count = sum(1 for v in weights.values() if v >= 1.5)
        extreme_factor_count = sum(1 for v in values if v <= 0.05 or v >= 0.95)

        issues: List[str] = []

        if maxed_weight_count >= 3:
            issues.append("Maximum number of elevated weights used. Confirm that priorities are genuine.")

        if variance < 0.002 and (sum(values) / len(values)) >= 0.90:
            issues.append("Assessment is uniformly very high. Check for self-serving optimism or missing risks.")

        if variance < 0.002 and (sum(values) / len(values)) <= 0.10:
            issues.append("Assessment is uniformly very low. Check for despair, protest scoring or strategic rejection.")

        if extreme_factor_count >= 5:
            issues.append("Many factor values are extreme. Human plausibility review recommended.")

        if H >= 0.90:
            issues.append("Humiliation risk is near maximum. Treat as acute instability signal.")

        signal = ReviewSignal.PLAUSIBILITY_REVIEW_REQUIRED if issues else ReviewSignal.OK

        return PlausibilityReview(
            party_name=assessment.name,
            signal=signal,
            issues=issues,
            factor_variance=round(variance, 6),
            maxed_weight_count=maxed_weight_count,
            extreme_factor_count=extreme_factor_count,
        )

    def validate_weights(self, weights: Dict[str, float]) -> Dict[str, float]:
        cleaned = {
            k: min(max(float(v), 1.0), 1.5)
            for k, v in weights.items()
            if k in POSITIVE_FACTORS
        }

        elevated = [k for k, v in cleaned.items() if v > 1.0]

        if len(elevated) > 3:
            top_three = sorted(elevated, key=lambda k: cleaned[k], reverse=True)[:3]
            cleaned = {k: (cleaned[k] if k in top_three else 1.0) for k in cleaned}

        return {f: cleaned.get(f, 1.0) for f in POSITIVE_FACTORS}

    def party_acceptance(self, assessment: PartyAssessment) -> float:
        weights = self.validate_weights(assessment.weights)
        weighted_sum = 0.0
        weight_total = 0.0

        for factor in POSITIVE_FACTORS:
            value = self.clamp(assessment.factors.get(factor, 0.0))
            weight = weights[factor]
            weighted_sum += value * weight
            weight_total += weight

        positive_mean = weighted_sum / weight_total if weight_total else 0.0
        H = self.clamp(assessment.humiliation_risk)
        return round(positive_mean * (1.0 - H), 4)

    def global_peace_value(
        self,
        p1: float,
        p2: float,
        mode: Optional[PeaceFormulaMode] = None,
    ) -> float:
        selected_mode = mode or self.peace_formula_mode
        asymmetry = abs(p1 - p2)

        if selected_mode == PeaceFormulaMode.STRICT_BALANCE:
            value = min(p1, p2) * (1.0 - asymmetry)
        elif selected_mode == PeaceFormulaMode.MINIMUM_ONLY:
            value = min(p1, p2)
        elif selected_mode == PeaceFormulaMode.WEIGHTED_BALANCE:
            value = min(p1, p2) * (1.0 - 0.5 * asymmetry)
        elif selected_mode == PeaceFormulaMode.AVERAGE_REFERENCE:
            value = ((p1 + p2) / 2.0) * (1.0 - asymmetry)
        else:
            raise ValueError(f"Unknown peace formula mode: {selected_mode}")

        return round(self.clamp(value), 4)

    def peace_compass(self, party1: PartyAssessment, party2: PartyAssessment) -> PeaceCompassResult:
        p1 = self.party_acceptance(party1)
        p2 = self.party_acceptance(party2)
        peace = self.global_peace_value(p1, p2)
        asymmetry = round(abs(p1 - p2), 4)
        weakest_party = party1.name if p1 <= p2 else party2.name

        if peace >= 0.75:
            stability = "STRONG_SIGNAL"
        elif peace >= 0.55:
            stability = "PROMISING_BUT_REQUIRES_REVIEW"
        elif peace >= 0.35:
            stability = "FRAGILE_REVISION_REQUIRED"
        else:
            stability = "CRITICAL_ASYMMETRY_OR_LOW_ACCEPTANCE"

        return PeaceCompassResult(
            p1_acceptance=p1,
            p2_acceptance=p2,
            peace_value=peace,
            weakest_party=weakest_party,
            asymmetry=asymmetry,
            stability_signal=stability,
            formula_mode=self.peace_formula_mode,
            formula_note=FORMULA_NOTES[self.peace_formula_mode],
        )

    def factor_gaps(self, party: PartyAssessment, threshold: float = 0.5) -> List[str]:
        return [
            factor for factor in POSITIVE_FACTORS
            if self.clamp(party.factors.get(factor, 0.0)) < threshold
        ]

    def recommendation_key(self, party_name: str, category: str) -> str:
        return f"{party_name.lower()}::{category.lower()}"

    def stable_issue_key(self, issue: str) -> str:
        key = re.sub(r"[^a-z0-9]+", "_", issue.lower()).strip("_")
        return key[:80] or "unknown_issue"

    def add_recommendation(
        self,
        recs: List[str],
        seen_keys: set,
        key: str,
        message: str,
    ) -> None:
        if key not in seen_keys:
            recs.append(message)
            seen_keys.add(key)

    def generate_recommendations(
        self,
        party1: PartyAssessment,
        party2: PartyAssessment,
        compass: PeaceCompassResult,
        audits: Dict[str, IntentAudit],
        mirrors: List[ConscienceMirror],
        plausibility_reviews: Dict[str, PlausibilityReview],
        suppress_factor_optimization: bool = False,
    ) -> List[str]:
        recs: List[str] = []
        seen_keys: set = set()

        if not suppress_factor_optimization:
            if compass.peace_value < 0.35:
                self.add_recommendation(
                    recs,
                    seen_keys,
                    "global::fragile_proposal",
                    "Do not optimise for agreement yet. The proposal is structurally fragile. "
                    "First reduce humiliation risk and improve the weakest party's acceptance."
                )

            if compass.asymmetry > 0.25:
                self.add_recommendation(
                    recs,
                    seen_keys,
                    "global::acceptance_asymmetry",
                    "Acceptance asymmetry is high. Avoid winner-loser framing. Rebalance the proposal before public communication."
                )

        for party in [party1, party2]:
            H = self.clamp(party.humiliation_risk)

            if H >= 0.75:
                self.add_recommendation(
                    recs,
                    seen_keys,
                    self.recommendation_key(party.name, "humiliation_critical"),
                    f"{party.name}: Humiliation risk is critical. Add face-saving language, security guarantees, "
                    "public dignity and a non-total-defeat narrative."
                )
            elif H >= 0.5:
                self.add_recommendation(
                    recs,
                    seen_keys,
                    self.recommendation_key(party.name, "humiliation_significant"),
                    f"{party.name}: Humiliation risk is significant. Reduce surrender, betrayal or blame signals."
                )

            if not suppress_factor_optimization:
                for gap in self.factor_gaps(party):
                    label = FACTOR_LABELS[gap]
                    self.add_recommendation(
                        recs,
                        seen_keys,
                        self.recommendation_key(party.name, f"factor_gap_{gap}"),
                        f"{party.name}: Strengthen {label}. This factor is currently below the recommended threshold."
                    )

        for mirror in mirrors:
            category = f"mirror_{mirror.profile.value}"
            if mirror.requires_36max:
                self.add_recommendation(
                    recs,
                    seen_keys,
                    self.recommendation_key(mirror.party_name, category),
                    f"{mirror.party_name}: Activate 36 MAX. Recommended action: {mirror.recommended_action}"
                )
            elif mirror.danger_level in [DangerLevel.HIGH, DangerLevel.MAXIMAL]:
                self.add_recommendation(
                    recs,
                    seen_keys,
                    self.recommendation_key(mirror.party_name, category),
                    f"{mirror.party_name}: Human review required. Recommended action: {mirror.recommended_action}"
                )

        for party_name, audit in audits.items():
            category = f"audit_{audit.profile.value}"
            if audit.danger_level in [DangerLevel.HIGH, DangerLevel.MAXIMAL]:
                mirror_key = self.recommendation_key(party_name, f"mirror_{audit.profile.value}")
                if mirror_key not in seen_keys:
                    self.add_recommendation(
                        recs,
                        seen_keys,
                        self.recommendation_key(party_name, category),
                        f"{party_name}: Human review required. The language indicates: {audit.issue}"
                    )

        for party_name, review in plausibility_reviews.items():
            if review.signal == ReviewSignal.PLAUSIBILITY_REVIEW_REQUIRED:
                self.add_recommendation(
                    recs,
                    seen_keys,
                    self.recommendation_key(party_name, "plausibility_review"),
                    f"{party_name}: Plausibility review required. Do not treat the numerical assessment as neutral input yet."
                )
                for issue in review.issues:
                    self.add_recommendation(
                        recs,
                        seen_keys,
                        self.recommendation_key(
                            party_name,
                            f"plausibility_issue_{self.stable_issue_key(issue)}",
                        ),
                        f"{party_name}: {issue}"
                    )

        return recs

    def process_conflict_input(
        self,
        party1_text: str,
        party2_text: str,
        party1_assessment: PartyAssessment,
        party2_assessment: PartyAssessment,
    ) -> KernelOutput:
        audit1 = self.audit_intent(party1_text)
        audit2 = self.audit_intent(party2_text)

        audits = {
            party1_assessment.name: audit1,
            party2_assessment.name: audit2,
        }

        nuance1 = self.nuance_review(party1_text, audit1)
        nuance2 = self.nuance_review(party2_text, audit2)
        nuance_reviews = {
            party1_assessment.name: nuance1,
            party2_assessment.name: nuance2,
        }

        truth_dignity1 = self.truth_dignity_review(party1_text)
        truth_dignity2 = self.truth_dignity_review(party2_text)
        truth_dignity_reviews = {
            party1_assessment.name: truth_dignity1,
            party2_assessment.name: truth_dignity2,
        }

        review1 = self.plausibility_review(party1_assessment)
        review2 = self.plausibility_review(party2_assessment)
        plausibility_reviews = {
            party1_assessment.name: review1,
            party2_assessment.name: review2,
        }

        mirrors = [
            self.conscience_mirror(party1_assessment.name, audit1),
            self.conscience_mirror(party2_assessment.name, audit2),
        ]

        emergency_protocol: List[str] = []
        if any(mirror.requires_36max for mirror in mirrors):
            trigger = next(
                (mirror.message for mirror in mirrors if mirror.requires_36max),
                "Acute escalation risk detected.",
            )
            emergency_protocol = self.run_36max_protocol(trigger)

        compass = self.peace_compass(party1_assessment, party2_assessment)
        pre_peace = self.pre_peace_stabilization(
            party1_assessment,
            party2_assessment,
            compass.p1_acceptance,
            compass.p2_acceptance,
        )

        recommendations = self.generate_recommendations(
            party1_assessment,
            party2_assessment,
            compass,
            audits,
            mirrors,
            plausibility_reviews,
            suppress_factor_optimization=pre_peace.required,
        )

        if pre_peace.required:
            recommendations.insert(0, f"Pre-peace stabilization required: {pre_peace.reason}")
            for step in pre_peace.steps:
                recommendations.append(f"Pre-peace step: {step}")

        for party_name, review in nuance_reviews.items():
            if review.signal == ReviewSignal.NUANCE_REVIEW_REQUIRED:
                recommendations.append(
                    f"{party_name}: Nuance review required. Emotional intensity detected without clear escalation; do not over-block."
                )

        for party_name, review in truth_dignity_reviews.items():
            if review.truth_is_painful or review.needless_humiliation_detected:
                recommendations.append(
                    f"{party_name}: Truth-dignity bridge: {review.suggested_bridge}"
                )

        system_statuses: List[str] = []
        if emergency_protocol:
            system_statuses.append("36MAX_DEESCALATION_REQUIRED")
        if pre_peace.required:
            system_statuses.append("PRE_PEACE_STABILIZATION_REQUIRED")
        if review1.signal == ReviewSignal.PLAUSIBILITY_REVIEW_REQUIRED or review2.signal == ReviewSignal.PLAUSIBILITY_REVIEW_REQUIRED:
            system_statuses.append("PLAUSIBILITY_REVIEW_REQUIRED")
        if not system_statuses:
            if compass.peace_value < 0.35:
                system_statuses.append("REVISION_REQUIRED")
            else:
                system_statuses.append("HUMAN_REVIEW_READY")

        if (
            "36MAX_DEESCALATION_REQUIRED" in system_statuses
            and "PRE_PEACE_STABILIZATION_REQUIRED" in system_statuses
        ):
            primary_status = "ACUTE_ESCALATION_AND_PRE_PEACE_STABILIZATION_REQUIRED"
        else:
            primary_status = system_statuses[0]

        return KernelOutput(
            system_status=primary_status,
            system_statuses=system_statuses,
            origin_axiom=self.origin.as_kernel_axiom(),
            origin_manifesto=self.origin.manifesto(),
            origin_story=self.origin.origin_story(),
            intent_audits={name: asdict(audit) for name, audit in audits.items()},
            nuance_reviews={name: asdict(review) for name, review in nuance_reviews.items()},
            truth_dignity_reviews={name: asdict(review) for name, review in truth_dignity_reviews.items()},
            plausibility_reviews={name: asdict(review) for name, review in plausibility_reviews.items()},
            pre_peace_stabilization=asdict(pre_peace),
            conscience_mirror=[asdict(mirror) for mirror in mirrors],
            emergency_protocol=emergency_protocol,
            peace_compass=asdict(compass),
            recommendations=recommendations,
            human_review_required=True,
        )


# =============================================================================
# 5. RUNTIME DEMO
# =============================================================================


if __name__ == "__main__":
    kernel = CopCode36MaxPeaceKernel(
        peace_formula_mode=PeaceFormulaMode.STRICT_BALANCE
    )

    party1_statement = (
        "We will sue the state and everyone responsible until they are completely ruined. "
        "This is our retaliation."
    )

    party2_statement = (
        "We will remain silent and avoid talking about the facts."
    )

    party1 = PartyAssessment(
        name="Party 1 / Injured Side",
        factors={
            "W": 0.20,
            "S": 0.20,
            "T": 0.30,
            "G": 0.10,
            "F": 0.20,
            "Z": 0.20,
            "V": 0.10,
        },
        humiliation_risk=0.95,
        weights={"T": 1.5, "F": 1.5, "S": 1.3},
    )

    party2 = PartyAssessment(
        name="Party 2 / Institution",
        factors={
            "W": 0.70,
            "S": 0.70,
            "T": 0.30,
            "G": 0.70,
            "F": 0.50,
            "Z": 0.60,
            "V": 0.40,
        },
        humiliation_risk=0.25,
        weights={"G": 1.3, "V": 1.3},
    )

    output = kernel.process_conflict_input(
        party1_text=party1_statement,
        party2_text=party2_statement,
        party1_assessment=party1,
        party2_assessment=party2,
    )

    print(json.dumps(asdict(output), indent=4, ensure_ascii=False))

