from composite_tag import CompositeTag
from leaf_tag import LeafTag


tag1 = LeafTag("tag1", {"test":"value", "test2":"val3"})
tag2 = LeafTag("tag2", {})

xmlDocument = CompositeTag("document", {}, [tag1, tag2])


xmlDocument.print()