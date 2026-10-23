from dataclass import dataclass
from pathllib import Path


@dataclass
class OCRResult:
    text: str
    confidence: float | None
    engine: str


class OCREngine:
    def recognize(self, image_path: Path)-> OCRResult:
        raise NotImplementedError(
            "OCR Engine msut implement the recognize method."
        )