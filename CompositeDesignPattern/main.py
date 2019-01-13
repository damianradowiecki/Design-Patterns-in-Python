from CompositeTag import CompositeTag
from LeafTag import LeafTag







tag1 = LeafTag("tag1", {})
tag2 = LeafTag("tag2", {})

xmlDocument = CompositeTag("document", {}, [tag1, tag2])


xmlDocument.print()