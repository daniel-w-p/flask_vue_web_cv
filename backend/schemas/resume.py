from .ma_init import MA

ma = MA.get()


class ResumeSchema(ma.Schema):
    """
    Resume schema
    """

    class Meta:
        pass


resume_schema = ResumeSchema()
resumes_schema = ResumeSchema(many=True)
