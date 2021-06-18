"""
https://beam.apache.org/releases/pydoc/2.29.0/apache_beam.transforms.util.html
"""

import apache_beam as beam

# Start with lists
emails_list = [
    ('amy', 'amy@example.com'),
    ('carl', 'carl@example.com'),
    ('julia', 'julia@example.com'),
    ('carl', 'carl@email.com'),
]
phones_list = [
    ('amy', '111-222-3333'),
    ('james', '222-333-4444'),
    ('amy', '333-444-5555'),
    ('carl', '444-555-6666'),
]

p = beam.Pipeline()

# Turn lists into pcollections
emails = p | 'CreateEmails' >> beam.Create(emails_list)
phones = p | 'CreatePhones' >> beam.Create(phones_list)


# Assign tags and CoGroupByKey your pcolls
# In results, tags will move into value section and values will become keys...
# docs: "Given an input dict of serializable keys (called “tags”) to 0 or more PCollections"
results = ({'emails_tag': emails, 'phones_tag': phones} | beam.CoGroupByKey()
)
(first, second) = results

results | beam.io.WriteToText('scratch.txt')
print('first' + str(first))
print('second' + str(second))

"""
===SAMPLE OUTPUT FROM ABOVE, scratch.txt====
('amy', {'emails_tag': ['amy@example.com'], 'phones_tag': ['111-222-3333', '333-444-5555']})
('james', {'emails_tag': [], 'phones_tag': ['222-333-4444']})
('carl', {'emails_tag': ['carl@example.com', 'carl@email.com'], 'phones_tag': ['444-555-6666']})
('julia', {'emails_tag': ['julia@example.com'], 'phones_tag': []})
"""

p.run()
