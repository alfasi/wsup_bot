import os

path = "/tmp/image.jpg"
group_id = ''

with open(os.path.expanduser('~/group_id')) as g_file:
    group_id = g_file.read().strip()

print("/L")
print("/group picture {} {}".format(group_id, path))
