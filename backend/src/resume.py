from ..core import Grad
from ..core import Links
from ..core import History


class Resume:
    title: str
    name: str
    address: str
    telephone: str
    email: str
    links: [Links]
    profile: str
    employment: [History]
    education: [History]
    additional: [History]
    skills: [Grad]
    tools: [str]
    languages: [Grad]
    interests: [str]

