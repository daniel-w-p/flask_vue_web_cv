class History:
    """
    Suitable for education and employment history
    """
    def __init__(self, where: str, when_from: str, when_to: str, what: str):
        """
        Init history
        :param where: string e.g. university name or company name
        :param when_from: string e.g. work start
        :param when_to: string e.g. graduation month-year
        :param what: string description
        """
        self.where = where
        self.when_from = when_from
        self.when_to = when_to
        self.what = what
