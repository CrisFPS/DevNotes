from pydantic import BaseModel


class ContentForm(BaseModel):
    title: str
    content: str = ""
    category: str = ""
    language: str = ""
    system: str = ""
    domain: str = ""
    object_type: str = ""
    is_business_rule: bool = False
    tags: str = ""

    def tags_list(self) -> list[str]:
        return [t.strip() for t in self.tags.split(",") if t.strip()]
