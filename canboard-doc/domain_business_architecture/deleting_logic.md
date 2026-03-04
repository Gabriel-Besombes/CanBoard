# Deleting logic

There are two problematics : deletion and archiving.

For now at least the approach will be this :

* Anything under the level of Card can be deleted without conditions and can't be archived.
* Cards can be archived without conditions. Cards can only be deleted once archived.
* Anything above a card can only be archived if all its contained elements are already archived and deleted once all its elements have been deleted and it has already been archived.

No cascading deletion or archiving.
