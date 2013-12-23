formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4);
print formatter % ("aaa", "bbb", "ccc", "ddd");
print formatter % (True, False, True, False);
print formatter % (formatter, formatter, formatter, formatter);
print formatter % (
			"another way",
			"aaa",
			"bbb",
			"ccc"
);

