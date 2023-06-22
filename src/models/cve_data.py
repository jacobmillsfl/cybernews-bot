from .json_serializable import JSONSerializable

class Description(JSONSerializable):
    def __init__(self, data: dict):
        self.lang = data.get('lang')
        self.value = data.get('value')


class CVSSMetric(JSONSerializable):
    def __init__(self, data: dict):
        cvss_data = data.get('cvssData').__dict__
        self.source = data.get('source')
        self.type = data.get('type')
        self.version = cvss_data.get('version')
        self.vector_string = cvss_data.get('vectorString')
        self.attack_vector = cvss_data.get('attackVector')
        self.attack_complexity = cvss_data.get('attackComplexity')
        self.privileges_required = cvss_data.get('privilegesRequired')
        self.user_interaction = cvss_data.get('userInteraction')
        self.scope = cvss_data.get('scope')
        self.confidentiality_impact = cvss_data.get('confidentialityImpact')
        self.integrity_impact = cvss_data.get('integrityImpact')
        self.availability_impact = cvss_data.get('availabilityImpact')
        self.base_score = cvss_data.get('baseScore')
        self.base_severity = cvss_data.get('baseSeverity')
        self.exploitability_score = data.get('exploitabilityScore')
        self.impact_score = data.get('impactScore')


class Weakness(JSONSerializable):
    def __init__(self, data: dict):
        self.source = data.get('source')
        self.type = data.get('type')
        description_data = data.get('description')
        self.description = [Description(d.__dict__) for d in description_data]


class Reference(JSONSerializable):
    def __init__(self, data: dict):
        self.url = data.get('url')
        self.source = data.get('source')


class CWE(JSONSerializable):
    def __init__(self, data):
        self.lang = data.get('lang')
        self.value = data.get('value')


class Vulnerability(JSONSerializable):
    def __init__(self, data):
        self.id = data.get('id')
        self.source_identifier = data.get('sourceIdentifier')
        self.published = data.get('published')
        self.last_modified = data.get('lastModified')
        self.vuln_status = data.get('vulnStatus')
        description_data = data.get('descriptions')
        self.descriptions = [Description(d.__dict__) for d in description_data]
        metrics_data = data.get('metrics', {}).__dict__.get('cvssMetricV31', [])
        self.metrics = [CVSSMetric(m.__dict__) for m in metrics_data]
        weaknesses_data = data.get('weaknesses', [])
        self.weaknesses = [Weakness(w.__dict__) for w in weaknesses_data]
        references_data = data.get('references', [])
        self.references = [Reference(r.__dict__) for r in references_data]
        cwe_data = data.get('cwe', [])
        self.cwe = [CWE(c.__dict__) for c in cwe_data]
        self.url = data.get('url')
        self.v31_score = data.get('v31score')
        self.v31_vector = data.get('v31vector')
        self.v31_severity = data.get('v31severity')
        self.v31_exploitability = data.get('v31exploitability')
        self.v31_impact_score = data.get('v31impactScore')
        self.score = data.get('score')
