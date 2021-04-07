from apps.tenant_db import models

import hypothesis.strategies as st
from hypothesis.extra.django import from_model

# This fuzzes all our models

max_examples=5

contact = from_model(
    models.Contact, 
    address=from_model(models.Building), 
    phone_number=st.text(
        max_size=10, 
        alphabet=st.characters(min_codepoint=1, max_codepoint=1000, blacklist_categories=('Cc', 'Cs'))
    )
)
contacts = st.lists(contact, min_size=1)

building = from_model(
    models.Building
)
buildings = st.lists(building, min_size=1)

activity = from_model(models.Activity, contact=contact)
activities = st.lists(activity, min_size=1)

