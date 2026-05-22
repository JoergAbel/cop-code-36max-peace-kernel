"""
COP CODE / 36 MAX AI Peace Kernel v3.1
====================================

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

Version 3.1 additions
---------------------
1. Modular intent analysis:
   - RegexIntentAnalyzer for transparent baseline detection.
   - SemanticIntentAnalyzer interface for future LLM or embedding-based analysis.
   - HybridIntentAnalyzer combines both layers without requiring an external model.

2. Plausibility review:
   - Detects suspiciously extreme, flat or self-serving assessments.
   - Flags PLAUSIBILITY_REVIEW_REQUIRED instead of accusing bad faith.

3. Calibration notice:
   - States clearly that the Peace Compass is a heuristic prototype, not a validated
     predictive model.

4. GitHub-ready framing:
   - Human review required.
   - No replacement for courts, diplomacy, mediation or historical responsibility.
   - Short technical manifesto in code.
   - Longer origin story separated for README or public explanation.

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
    PLAUSIBILITY_REVIEW_REQUIRED = "PLAUSIBILITY_REVIEW_REQUIRED"
    HUMAN_REVIEW_REQUIRED = "HUMAN_REVIEW_REQUIRED"


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
        Optional weights for up to three factors. Recommended range: 1.0 to 1.5.
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
    calibration_notice: str = CALIBRATION_NOTICE


@dataclass
class KernelOutput:
    system_status: str
    origin_axiom: Dict[str, str]
    origin_manifesto: str
    origin_story: str
    intent_audits: Dict[str, Dict[str, Any]]
    plausibility_reviews: Dict[str, Dict[str, Any]]
    conscience_mirror: List[str]
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
                r"\bsilence\b", r"\bsweep.*under.*rug\b",
                r"\bdon't talk about it\b", r"\bignore it\b",
                r"\bwhatever\b", r"\btotschweigen\b",
                r"\bunter den teppich\b", r"\beinfach vergessen\b",
            ],
            IntentProfile.HUMILIATION_RISK: [
                r"\bcapitulation\b", r"\bsurrender\b", r"\btraitor\b",
                r"\bhumiliation\b", r"\bkapitulation\b", r"\bverrat\b",
                r"\bdemütigung\b", r"\bgesichtsverlust\b",
            ],
            IntentProfile.TRUTH_SUPPRESSION: [
                r"\bhide the truth\b", r"\bdeny the facts\b",
                r"\bcover up\b", r"\bwahrheit verschweigen\b",
                r"\bfakten leugnen\b", r"\bvertuschen\b",
            ],
            IntentProfile.IDENTITY_THREAT: [
                r"\bthey are not a real people\b", r"\bthey have no right to exist\b",
                r"\bexistenzrecht absprechen\b", r"\bkeine echte nation\b",
            ],
            IntentProfile.DEHUMANIZATION: [
                r"\banimals\b", r"\bvermin\b", r"\bparasites\b",
                r"\btiere\b", r"\bungeziefer\b", r"\bparasiten\b",
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


class SemanticIntentAnalyzer:
    """
    Optional semantic analyzer interface.

    This class can be connected to:
        - a local embedding model,
        - an on-device classifier,
        - or an LLM-based classification function.

    The callable must accept a text string and return an IntentAudit.

    If no classifier is provided, this analyzer performs a small transparent
    heuristic check for indirect escalation phrases. It is intentionally modest:
    real semantic classification should be added by the implementer.
    """

    def __init__(self, classifier: Optional[Callable[[str], IntentAudit]] = None):
        self.classifier = classifier
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
        if self.classifier is not None:
            return self.classifier(text)

        text_lc = text.lower()
        matches = [phrase for phrase in self.indirect_escalation_phrases if phrase in text_lc]

        if matches:
            return IntentAudit(
                profile=IntentProfile.RETALIATION_LOOP,
                danger_level=DangerLevel.HIGH,
                issue="Indirect semantic escalation pattern detected.",
                matched_terms=matches,
                source="semantic_heuristic",
                confidence=0.6,
            )

        return IntentAudit(
            profile=IntentProfile.CONSTRUCTIVE,
            danger_level=DangerLevel.LOW,
            issue="No semantic escalation pattern detected by fallback heuristic.",
            matched_terms=[],
            source="semantic_heuristic",
            confidence=0.25,
        )


class HybridIntentAnalyzer:
    """
    Combines regex and semantic analysis.

    The more serious audit wins. This allows transparent regex detection while
    leaving room for future semantic models.
    """

    def __init__(self, semantic_classifier: Optional[Callable[[str], IntentAudit]] = None):
        self.regex = RegexIntentAnalyzer()
        self.semantic = SemanticIntentAnalyzer(semantic_classifier)

    @staticmethod
    def danger_rank(level: DangerLevel) -> int:
        return {
            DangerLevel.LOW: 0,
            DangerLevel.MEDIUM: 1,
            DangerLevel.HIGH: 2,
            DangerLevel.MAXIMAL: 3,
        }[level]

    def analyze(self, text: str) -> IntentAudit:
        regex_audit = self.regex.analyze(text)
        semantic_audit = self.semantic.analyze(text)

        if self.danger_rank(semantic_audit.danger_level) > self.danger_rank(regex_audit.danger_level):
            return semantic_audit

        if self.danger_rank(semantic_audit.danger_level) == self.danger_rank(regex_audit.danger_level):
            if semantic_audit.confidence > regex_audit.confidence:
                return semantic_audit

        return regex_audit


# =============================================================================
# 4. COP CODE PEACE KERNEL
# =============================================================================


class CopCode36MaxPeaceKernel:
    """
    A modular AI de-escalation layer.

    The kernel does five things:
        1. Preserves the origin story: Abel Error -> 36 MAX Correction.
        2. Audits language for retaliation, humiliation, dehumanization and truth suppression.
        3. Reviews plausibility of party assessments without shaming or accusing.
        4. Runs the Peace Compass calculation.
        5. Generates de-escalation recommendations for human review.
    """

    def __init__(self, intent_analyzer: Optional[IntentAnalyzer] = None):
        self.origin = OriginLayer()
        self.intent_analyzer = intent_analyzer or HybridIntentAnalyzer()
        self.truth_foundation = {
            "facts_priority": True,
            "no_hallucinations": True,
            "transparency_required": True,
            "human_review_required": True,
            "dignity_without_truth_is_empty": True,
            "deescalation_without_justice_is_unstable": True,
            "heuristic_not_verdict": True,
        }

    # -------------------------------------------------------------------------
    # Utility methods
    # -------------------------------------------------------------------------

    @staticmethod
    def clamp(value: float) -> float:
        return max(0.0, min(1.0, float(value)))

    # -------------------------------------------------------------------------
    # Intent audit and conscience mirror
    # -------------------------------------------------------------------------

    def audit_intent(self, text: str) -> IntentAudit:
        """
        Detects whether a conflict statement risks pulling the system into the
        Cain Loop: retaliation, blame fixation, dehumanization, humiliation or truth suppression.

        This is a heuristic early-warning layer, not a moral verdict.
        """
        return self.intent_analyzer.analyze(text)

    def conscience_mirror(self, audit: IntentAudit) -> str:
        """
        Mirrors the systemic consequence of the detected pattern.
        The mirror does not shame the user. It interrupts escalation.
        """
        if audit.profile == IntentProfile.DEHUMANIZATION:
            return (
                "Dehumanization detected: this is an acute Cain Loop amplifier. "
                "The system must not normalize language that turns people into objects, animals or vermin. "
                "36 MAX response: stop escalation, restore human dignity, preserve truth and move to human review."
            )

        if audit.profile == IntentProfile.RETALIATION_LOOP:
            return (
                "Cain Loop detected: pain is trying to become retaliation. "
                "The Abel Error would repeat itself if the system optimised for revenge, "
                "annihilation or humiliation. 36 MAX response: pause escalation, protect truth, "
                "and search for a second-chance path."
            )

        if audit.profile == IntentProfile.EXTERNAL_BLAME_LOOP:
            return (
                "External blame loop detected: the system may be converting trauma "
                "into endless legal or political war. The COP CODE does not erase "
                "responsibility, but it asks whether the same energy can be transformed "
                "into a tool that prevents future harm."
            )

        if audit.profile == IntentProfile.TRUTH_SUPPRESSION:
            return (
                "Truth suppression detected: de-escalation cannot be purchased by denying facts. "
                "Dignity without truth is empty; peace without responsibility is unstable."
            )

        if audit.profile == IntentProfile.IDENTITY_THREAT:
            return (
                "Identity threat detected: denying a group's existence or legitimacy can lock conflict into survival mode. "
                "The system should move from identity negation to safety, recognition and verifiable guarantees."
            )

        if audit.profile == IntentProfile.HUMILIATION_RISK:
            return (
                "Humiliation risk detected: a solution that feels like surrender, betrayal or public defeat "
                "will likely remain unstable. Add face-saving language and credible security."
            )

        if audit.profile == IntentProfile.FAKED_PEACE:
            return (
                "Fake peace risk detected: silence is not resolution. The system should surface truth gently, "
                "before suppressed conflict returns as escalation."
            )

        return "No conscience warning. Continue with dignity, truth and human review."

    # -------------------------------------------------------------------------
    # 36 MAX emergency protocol
    # -------------------------------------------------------------------------

    def run_36max_protocol(self, trigger: str) -> List[str]:
        """
        Symbolic 36-minute reanimation sequence for acute escalation.
        This is not a medical claim. It is a conflict-resuscitation metaphor.
        """
        return [
            f"36 MAX activated: {trigger}",
            "01-10: Stop escalation. Freeze retaliation, humiliation, dehumanization and irreversible action.",
            "11-20: Separate identity from position. No party is reduced to guilt, shame or victory.",
            "21-30: Establish truth foundation. Name facts, harm, responsibility, fears and red lines.",
            "31-35: Search for a second-chance corridor: dignity, safety, justice, face-saving and future.",
            "36: Return to human decision with de-escalated options. The system proposes; humans decide.",
        ]

    # -------------------------------------------------------------------------
    # Plausibility review
    # -------------------------------------------------------------------------

    def plausibility_review(self, assessment: PartyAssessment) -> PlausibilityReview:
        """
        Detects suspiciously extreme or flat assessments.

        This does not accuse bad faith. It flags the assessment for human review.
        In conflict settings, extreme input can mean manipulation, trauma, fear,
        misunderstanding or strategic communication. The system must not shame it.
        """
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

    # -------------------------------------------------------------------------
    # Peace Compass calculation
    # -------------------------------------------------------------------------

    def validate_weights(self, weights: Dict[str, float]) -> Dict[str, float]:
        """
        Friedenskompass rule: up to three factors may receive elevated weighting.
        Elevated values are capped at 1.5.
        All positive factors are guaranteed to exist in the returned dictionary.
        """
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

    def global_peace_value(self, p1: float, p2: float) -> float:
        return round(min(p1, p2) * (1.0 - abs(p1 - p2)), 4)

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
        )

    # -------------------------------------------------------------------------
    # Recommendation engine
    # -------------------------------------------------------------------------

    def factor_gaps(self, party: PartyAssessment, threshold: float = 0.5) -> List[str]:
        return [
            factor for factor in POSITIVE_FACTORS
            if self.clamp(party.factors.get(factor, 0.0)) < threshold
        ]

    def generate_recommendations(
        self,
        party1: PartyAssessment,
        party2: PartyAssessment,
        compass: PeaceCompassResult,
        audits: Dict[str, IntentAudit],
        plausibility_reviews: Dict[str, PlausibilityReview],
    ) -> List[str]:
        recs: List[str] = []

        if compass.peace_value < 0.35:
            recs.append(
                "Do not optimise for agreement yet. The proposal is structurally fragile. "
                "First reduce humiliation risk and improve the weakest party's acceptance."
            )

        if compass.asymmetry > 0.25:
            recs.append(
                "Acceptance asymmetry is high. Avoid winner-loser framing. Rebalance the proposal before public communication."
            )

        for party in [party1, party2]:
            H = self.clamp(party.humiliation_risk)

            if H >= 0.75:
                recs.append(
                    f"{party.name}: Humiliation risk is critical. Add face-saving language, security guarantees, "
                    "public dignity and a non-total-defeat narrative."
                )
            elif H >= 0.5:
                recs.append(
                    f"{party.name}: Humiliation risk is significant. Reduce surrender, betrayal or blame signals."
                )

            for gap in self.factor_gaps(party):
                label = FACTOR_LABELS[gap]
                recs.append(
                    f"{party.name}: Strengthen {label}. This factor is currently below the recommended threshold."
                )

        for party_name, audit in audits.items():
            if audit.danger_level in [DangerLevel.HIGH, DangerLevel.MAXIMAL]:
                recs.append(
                    f"{party_name}: Activate 36 MAX before proposing solutions. The language indicates: {audit.issue}"
                )

        for party_name, review in plausibility_reviews.items():
            if review.signal == ReviewSignal.PLAUSIBILITY_REVIEW_REQUIRED:
                recs.append(
                    f"{party_name}: Plausibility review required. Do not treat the numerical assessment as neutral input yet."
                )
                for issue in review.issues:
                    recs.append(f"{party_name}: {issue}")

        seen = set()
        unique_recs = []
        for rec in recs:
            if rec not in seen:
                unique_recs.append(rec)
                seen.add(rec)
        return unique_recs

    # -------------------------------------------------------------------------
    # Main process
    # -------------------------------------------------------------------------

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

        review1 = self.plausibility_review(party1_assessment)
        review2 = self.plausibility_review(party2_assessment)
        plausibility_reviews = {
            party1_assessment.name: review1,
            party2_assessment.name: review2,
        }

        mirrors = [
            f"{party1_assessment.name}: {self.conscience_mirror(audit1)}",
            f"{party2_assessment.name}: {self.conscience_mirror(audit2)}",
        ]

        emergency_protocol: List[str] = []
        if audit1.danger_level == DangerLevel.MAXIMAL or audit2.danger_level == DangerLevel.MAXIMAL:
            trigger = audit1.issue if audit1.danger_level == DangerLevel.MAXIMAL else audit2.issue
            emergency_protocol = self.run_36max_protocol(trigger)

        compass = self.peace_compass(party1_assessment, party2_assessment)

        recommendations = self.generate_recommendations(
            party1_assessment,
            party2_assessment,
            compass,
            audits,
            plausibility_reviews,
        )

        if emergency_protocol:
            status = "36MAX_DEESCALATION_REQUIRED"
        elif review1.signal == ReviewSignal.PLAUSIBILITY_REVIEW_REQUIRED or review2.signal == ReviewSignal.PLAUSIBILITY_REVIEW_REQUIRED:
            status = "PLAUSIBILITY_REVIEW_REQUIRED"
        elif compass.peace_value < 0.35:
            status = "REVISION_REQUIRED"
        else:
            status = "HUMAN_REVIEW_READY"

        return KernelOutput(
            system_status=status,
            origin_axiom=self.origin.as_kernel_axiom(),
            origin_manifesto=self.origin.manifesto(),
            origin_story=self.origin.origin_story(),
            intent_audits={name: asdict(audit) for name, audit in audits.items()},
            plausibility_reviews={name: asdict(review) for name, review in plausibility_reviews.items()},
            conscience_mirror=mirrors,
            emergency_protocol=emergency_protocol,
            peace_compass=asdict(compass),
            recommendations=recommendations,
            human_review_required=True,
        )


# =============================================================================
# 5. RUNTIME DEMO
# =============================================================================


if __name__ == "__main__":
    kernel = CopCode36MaxPeaceKernel()

    # Demo scenario:
    # A traumatic event risks being converted into revenge, blame and legal annihilation.
    # The 36 MAX correction asks whether the energy can be transformed into a peace tool.
    # In real use, replace demo data with human-reviewed assessments.
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
