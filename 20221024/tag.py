tag_data = {
    "a": [      "a:1"],
    "b": ["#a", "b:1"],
    "c": ["#b", "c:1"],
}

test_data = {
    "a": ["#b", "a:1"],
    "b": ["#c", "b:1"],
    "c": ["#a", "c:1"],
}

def get_item_from_tag(tag_id, source, _source_tags = None):
    _source_tags, _tags = _source_tags or [], []
    for tag in source[tag_id]:
        if tag[0] == "#":
            if tag in _source_tags:
                continue
            _source_tags.append(tag)
            _tags += get_item_from_tag(tag[1:], source, _source_tags)
        else:
            _tags.append(tag)
    return [*{*_tags}]

def show_result(tags):
    for tag in tags:
        print(tag, get_item_from_tag(tag, tags))
    print()

show_result(tag_data)
show_result(test_data)