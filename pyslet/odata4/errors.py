#! /usr/bin/env python


class ODataError(Exception):

    """Base error for OData exceptions"""
    pass


class ModelError(ODataError):

    """Base error for model exceptions"""
    pass


class DuplicateNameError(ModelError):

    """Raised when a duplicate name is encountered in a name table"""
    pass


class ObjectNotDeclaredError(ModelError):

    """Raised when an operation on an object is not permitted because
    the object has *not* been declared"""
    pass


class ObjectDeclaredError(ModelError):

    """Raised when an operation on an object is not permitted because
    the object has *already* been declared"""
    pass


class UndeclarationError(ModelError):

    """Raised when an attempt is made to undeclare a name in a name
    table"""
    pass


class NameTableClosed(ModelError):

    """Raised when an attempt to declare a name in a closed name table
    is made"""
    pass


class InheritanceCycleDetected(ModelError):

    """Raised when an inheritance cycle is detected in a model."""
    pass


class PathError(Exception):

    """Raised during path traversal"""
    pass


class Requirement(object):

    """Human friendly messages

    Each requirement in the OData specification is transcribed into a
    message string and defined as an attribute of this object.  This
    makes the code easier to read and facilitates the wholescale
    substitution of the messages for unittesting (and potentially
    translation, should the specification be translated into languages
    other than English)."""
    pass


class Req40(object):

    """OData 4.0 reference messages

    Used by unit tests to ensure correct error messages are being
    generated for invalid CSDL test cases."""
    pass


# Section 3: Entity Model Wrapper

Requirement.csdl_root = (
    "A CSDL document MUST contain a root edmx:Edmx element")
Req40.csdl_root = "4.0 P3 3.1 #1"

Requirement.csdl_data_services = (
    "[The root] element MUST contain a single direct child "
    "edmx:DataServices element")
Req40.csdl_data_services = "4.0 P3 3.1 #2"

Requirement.edmx_version = (
    "The edmx:Edmx element MUST provide the value 4.0 for the "
    "Version attribute")
Req40.edmx_version = "4.0 P3 3.1.1"

Requirement.schemas = (
    "The edmx:DataServices element MUST contain one or more edm:Schema "
    "elements")
Req40.schemas = "4.0 P3 3.2"

Requirement.reference = (
    "The edmx:Reference element MUST contain at least one edmx:Include or "
    "edmx:IncludeAnnotations child element")
Req40.reference = "4.0 P3 3.3"

Requirement.reference_uri = (
    "The edmx:Reference element MUST specify a Uri attribute")
Req40.reference_uri = "4.0 P3 3.3.1 #1"

Requirement.unique_reference = (
    "Two references MUST NOT specify the same URI")
Req40.unique_reference = "4.0 P3 3.3.1 #2"

Requirement.include_namespace = (
    "The edmx:Include element MUST provide a Namespace value for the "
    "Namespace attribute")
Req40.include_namespace = "4.0 P3 3.4.1 #1"

Requirement.include_schema_s = (
    "The value [of the Namespace attribute] MUST match the namespace of a "
    "schema defined in the referenced CSDL document (%s)")
Req40.include_schema_s = "4.0 P3 3.4.1 #2 (%s)"

Requirement.unique_include_s = (
    "The same namespace MUST NOT be included more than once (%s)")
Req40.unique_include_s = "4.0 P3 3.4.1 #3 (%s)"

Requirement.unique_namespace_s = (
    "A document MUST NOT assign the same alias to different namespaces and "
    "MUST NOT specify an alias with the same name as an in-scope "
    "namespace (%s)")
Req40.unique_namespace_s = "4.0 P3 3.4.2 #1 (%s)"

Requirement.reserved_namespace_s = (
    "The Alias attribute MUST NOT use the reserved values Edm, odata, "
    "System, or Transient (%s)")
Req40.reserved_namespace_s = "4.0 P3 3.4.2 #2 (%s)"

Requirement.term_namespace = (
    "An edmx:IncludeAnnotations element MUST provide a Namespace value for "
    "the TermNamespace attribute")
Req40.term_namespace = "4.0 P3 3.5.1"


# Section 4: Common Characteristics of Entity Models

Requirement.type_name = (
    "A nominal type has a name that MUST be a SimpleIdentifier")
Req40.type_name = "4.0 P3 4.1 #1"


Requirement.type_qname_s = (
    "The qualified type name MUST be unique within a model (%s)")
Req40.type_qname_s = (
    "4.0 P3 4.1 #2; 4.0 P3 5.1.1 #3; 4.0 P3 8.1.1 #2; 4.0 P3 9.1.1 #2; "
    "4.0 P3 10.1.1 #2; 4.0 P3 11.1.1 #2 (%s)")

# UNTESTED - violations are indistinguishable from the use of undeclared
# names
Requirement.type_ref = (
    "When referring to nominal types, the reference MUST use a "
    "Namespace-qualified name or an Alias-qualified name")
Req40.type_ref = "4.0 P3 4.1 #3"

Requirement.annotations_s = (
    "A model element MUST NOT specify more than one annotation for a "
    "given combination of Term and Qualifier attributes (%s)")
Req40.annotations_s = "4.0 P3 4.6 (%s)"


# Section 5: Schema

Requirement.unique_schema_child_s = (
    "Values of the Name attribute MUST be unique across all direct child "
    "elements of a schema (%s)")
Req40.unique_schema_child_s = "4.0 P3 5.1 (%s)"

Requirement.schema_name = (
    "All edm:Schema elements MUST have a namespace defined through a "
    "Namespace attribute")
Req40.schema_name = "4.0 P3 5.1.1 #1"

Requirement.schema_unique_s = (
    "The Schema Namespace attribute MUST be unique within the document (%s)")
Req40.schema_unique_s = "4.0 P3 5.1.1 #2 (%s)"

# Never raised: identical to Requirement.type_qname_s
Requirement.type_unique = (
    "Identifiers that are used to name types MUST be unique within a "
    "namespace")
Req40.type_unique = "4.0 P3 5.1.1 #3"

Requirement.reserved_schema_s = (
    "The Namespace attribute MUST NOT use the reserved values Edm, odata, "
    "System, or Transient (%s)")
Req40.reserved_schema_s = "4.0 P3 5.1.1 #4 (%s)"

Requirement.unique_alias_s = (
    "All edmx:Include and edm:Schema elements within a document MUST specify "
    "different values for the Alias attribute (%s)")
Req40.unique_alias_s = "4.0 P3 5.1.2 #1 (%s)"

Requirement.reserved_alias_s = (
    "The Alias attribute MUST NOT use the reserved values Edm, odata, "
    "System, or Transient (%s)")
Req40.reserved_alias_s = "4.0 P3 5.1.2 #2 (%s)"


# Section 6: Structural Property

# Never raised, see Requirement.property_unique_s
Requirement.property_unique = (
    "A property MUST specify a unique name")
Req40.property_unique = "4.0 P3 6.1 #1"

# Never raised, see Requirement.property_type_s
Requirement.property_type = (
    "A property MUST specify a type")
Req40.property_type = "4.0 P3 6.1 #2"

Requirement.property_name = (
    "The edm:Property element MUST include a Name attribute whose value "
    "is a SimpleIdentifier")
Req40.property_name = "4.0 P3 6.1.1 #1"

Requirement.property_unique_s = (
    "The name of the property MUST be unique within the set of "
    "structural and navigation properties of the containing structured "
    "type and any of its base types (%s)")
Req40.property_unique_s = (
    "4.0 P3 6.1 #1; 4.0 P3 6.1.1 #2; 4.0 P3 7.1.1 #2; 4.0 P3 8 #1 (%s)")

Requirement.property_type_s = (
    "The edm:Property element MUST include a Type attribute (%s)")
Req40.property_type_s = "4.0 P3 6.1 #2; 4.0 P3 6.1.2 #1 (%s)"

Requirement.property_type_declared_s = (
    "The value of the Type attribute MUST be the QualifiedName of a "
    "primitive type, complex type, or enumeration type in scope, or a "
    "collection of one of these types (%s)")
Req40.property_type_declared_s = "4.0 P3 6.1.2 #2 (%s)"

# TODO
Requirement.property_coll_exists = (
    "If the edm:Property element contains a Type attribute that specifies "
    "a collection, the property MUST always exist")
Req40.property_coll_exists = "4.0 P3 6.2.1 #1"

Requirement.decimal_precision = (
    "For a decimal property the Precision MUST be a positive integer")
Req40.decimal_precision = "4.0 P3 6.2.3 #1"

Requirement.temporal_precision = (
    "For a temporal property the Precision MUST be a non-negative integer "
    "between zero and twelve")
Req40.temporal_precision = "4.0 P3 6.2.3 #2"

# Probably untestable at runtime
Requirement.data_loss_precision = (
    "Client developers MUST be aware of the potential for data loss when "
    "round-tripping values of greater precision")
Req40.data_loss_precision = "4.0 P3 6.2.3 #3"

Requirement.scale_gt_precision = (
    "The value of the Scale attribute MUST be less than or equal to the "
    "value of the Precision attribute")
Req40.scale_gt_precision = "4.0 P3 6.2.4"

Requirement.srid_value = (
    "The value of the SRID attribute MUST be a non-negative integer or "
    "the special value variable")
Req40.srid_value = "4.0 P3 6.2.6"

# Never raised, the XML parser will fail if attribute values are invalid
Requirement.string_escape = (
    "Default values of type Edm.String MUST be represented according to the "
    "XML escaping rules for character data in attribute values")
Req40.string_escape = "4.0 P3 6.2.7 #1"

Requirement.primitive_default_s = (
    "Values of other primitive types MUST be represented according to the "
    "appropriate alternative in the primitiveValue rule (%s)")
Req40.primitive_default_s = "4.0 P3 6.2.7 #2 (%s)"


# Section 7: Navigation Property

Requirement.nav_name = (
    "The edm:NavigationProperty element MUST include a Name attribute whose "
    "value is a SimpleIdentifier")
Req40.nav_name = "4.0 P3 7.1.1 #1"

# Never raised, see Requirement.property_unique_s
Requirement.nav_unique = (
    "The name of the navigation property MUST be unique within the set of "
    "structural and navigation properties of the containing structured type "
    "and any of its base types")
Req40.nav_name = "4.0 P3 7.1.1 #2"

Requirement.nav_type_s = (
    "The edm:NavigationProperty element MUST include a Type attribute (%s)")
Req40.nav_type_s = "4.0 P3 7.1.2 #1 (%s)"

Requirement.nav_type_resolved_s = (
    "The value of the type attribute MUST resolve to an entity type or a "
    "collection of an entity type (%s)")
Req40.nav_type_resolved_s = "4.0 P3 7.1.2 #2 (%s)"

# TODO
Requirement.nav_type_related = (
    "The related entities MUST be of the specified entity type or one of "
    "its subtypes")
Req40.nav_type_resolved_s = "4.0 P3 7.1.2 #3"

Requirement.nav_collection_exists_s = (
    "A navigation property whose Type attribute specifies a collection "
    "MUST NOT specify a value for the Nullable attribute (%s)")
Req40.nav_collection_exists_s = "4.0 P3 7.1.3 (%s)"

Requirement.nav_partner_complex_s = (
    "The Partner attribute MUST NOT be specified for navigation properties "
    "of complex types (%s)")
Req40.nav_partner_complex_s = "4.0 P3 7.1.4 #1 (%s)"

Requirement.nav_partner_path_s = (
    "The Partner attribute MUST be a path from the entity type specified in "
    "the Type attribute to a navigation property defined on that type or a "
    "derived type (%s)")
Req40.nav_partner_path_s = "4.0 P3 7.1.4 #2 (%s)"

Requirement.nav_partner_nav_s = (
    "The Partner path MUST NOT traverse any navigation properties (%s)")
Req40.nav_partner_nav_s = "4.0 P3 7.1.4 #3 (%s)"

Requirement.nav_partner_type_s = (
    "The type of the partner navigation property MUST be the containing "
    "entity type of the current navigation property or one of its parent "
    "entity types (%s)")
Req40.nav_partner_type_s = "4.0 P3 7.1.4 #4 (%s)"

# TODO
Requirement.nav_partner_backlink = (
    "The partner navigation property MUST lead back to the source entity "
    "from all related entities")
Req40.nav_partner_backlink = "4.0 P3 7.1.4 #5"

# TODO
Requirement.nav_partner_multilink = (
    "If the Partner attribute identifies a multivalued navigation property, "
    "the source entity MUST be part of that collection")
Req40.nav_partner_multilink = "4.0 P3 7.1.4 #6"

Requirement.nav_partner_bidirection_s = (
    "The partner navigation property MUST either specify the current "
    "navigation property as its partner or it MUST NOT specify a partner "
    "attribute (%s)")
Req40.nav_partner_bidirection_s = "4.0 P3 7.1.4 #7 (%s)"

Requirement.nav_contains_s = (
    "Complex types declaring a containment navigation property MUST NOT "
    "be used as the type of a collection-valued property")
Req40.nav_contains_s = "4.0 P3 7.1.5 #1 (%s)"

Requirement.nav_contains_binding_s = (
    "Containment navigation properties MUST NOT be specified as the last "
    "path segment in the Path attribute of a navigation property binding (%s)")
Req40.nav_contains_binding_s = "4.0 P3 7.1.5 #2 (%s)"

Requirement.nav_rcontains_s = (
    "If the containment is recursive, the partner navigation property MUST "
    "be nullable and specify a single entity type (%s)")
Req40.nav_rcontains_s = "4.0 P3 7.1.5 #3 (%s)"

Requirement.nav_nrcontains_s = (
    "If the containment is not recursive, the partner navigation property "
    "MUST NOT be nullable (%s)")
Req40.nav_nrcontains_s = "4.0 P3 7.1.5 #4 (%s)"

Requirement.nav_multi_contains_s = (
    "An entity type hierarchy MUST NOT contain more than one navigation "
    "property with a Partner attribute referencing a containment "
    "relationship (%s)")
Req40.nav_multi_contains_s = "4.0 P3 7.1.5 #5 (%s)"

# TODO
Requirement.ref_constraint_s = (
    "A referential constraint asserts that the dependent property MUST "
    "have the same value as the principal property (%s)")
Req40.ref_constraint_s = "4.0 P3 7.2 #1 (%s)"

Requirement.refcon_match_s = (
    "The type of the dependent property MUST match the type of the "
    "principal property (%s)")
Req40.refcon_match_s = "4.0 P3 7.2 #2; 4.0 P3 7.2.2 #3 (%s)"

Requirement.refcon_match_null_s = (
    "If the navigation property on which the referential constraint is "
    "defined or the principal property is nullable, then the dependent "
    "property MUST be nullable (%s)")
Req40.refcon_match_null_s = "4.0 P3 7.2 #3 (%s)"

Requirement.refcon_match_notnull_s = (
    "If both the navigation property and the principal property are not "
    "nullable, then the dependent property MUST be marked with the "
    "Nullable=\"false\" attribute value (%s)")
Req40.refcon_match_notnull_s = "4.0 P3 7.2 #4 (%s)"

Requirement.refcon_property_s = (
    "A referential constraint MUST specify a value for the Property "
    "attribute (%s)")
Req40.refcon_property_s = "4.0 P3 7.2.1 #1 (%s)"

Requirement.refcon_ppath_s = (
    "The Property attribute value MUST be a path expression resolving to "
    "a primitive property of the dependent entity type (%s)")
Req40.refcon_ppath_s = "4.0 P3 7.2.1 #2 (%s)"

Requirement.refcon_refprop_s = (
    "A referential constraint MUST specify a value for the "
    "ReferencedProperty attribute (%s)")
Req40.refcon_refprop_s = "4.0 P3 7.2.2 #1 (%s)"

Requirement.refcon_rppath_s = (
    "The ReferenceProperty attribute value MUST be a path expression "
    "resolving to a primitive property of the principal entity type (%s)")
Req40.refcon_rppath_s = "4.0 P3 7.2.2 #2 (%s)"

# Never raised: identical to Requirement.refcon_match_s
Requirement.refcon_rptype_s = (
    "The ReferencedProperty MUST have the same data type as the property "
    "of the dependent entity type (%s)")
Req40.refcon_rptype_s = "4.0 P3 7.2.2 #3 (%s)"

Requirement.ondelete_value = (
    "The edm:OnDelete element MUST include the Action attribute with "
    "one of the following values: Cascade, None, SetNull or SetDefault")
Req40.ondelete_value = "4.0 P3 7.2.3"


# Section 8: Entity Type

# Never raised: covered by Requirement.property_unique_s
Requirement.et_unique_names = (
    "All properties MUST have a unique name within an entity type.")
Req40.et_unique_names = "4.0 P3 8 #1"

Requirement.et_same_name_s = (
    "Properties MUST NOT have the same name as the declaring entity "
    "type (%s)")
Req40.et_same_name_s = "4.0 P3 8 #2 (%s)"

Requirement.et_name = (
    "The edm:EntityType element MUST include a Name attribute whose value "
    "is a SimpleIdentifier")
Req40.et_name = "4.0 P3 8.1.1 #1"

# Never raised: identical to Requirement.type_qname_s
Requirement.et_name_unique_s = (
    "The EntityType name MUST be unique within its namespace (%s)")
Req40.et_name_unique_s = "4.0 P3 8.1.1 #2 (%s)"

Requirement.et_cycle_s = (
    "An entity type MUST NOT introduce an inheritance cycle via the base "
    "type attribute (%s)")
Req40.et_cycle_s = "4.0 P3 8.1.2 (%s)"

Requirement.et_abstract_key_s = (
    "A non-abstract entity type MUST define a key or derive from a base "
    "type with a defined key (%s)")
Req40.et_abstract_key_s = "4.0 P3 8.1.3 #1; 4.0 P3 8.2 #1 (%s)"

Requirement.et_abstract_base_s = (
    "An abstract entity type MUST NOT inherit from a non-abstract entity "
    "type (%s)")
Req40.et_abstract_base_s = "4.0 P3 8.1.3 #2 (%s)"

Requirement.et_open_base_s = (
    "An entity type derived from an open entity type MUST NOT provide a "
    "value of false for the OpenType attribute (%s)")
Req40.et_open_base_s = "4.0 P3 8.1.4 #1 (%s)"

# Never raised: we don't validate clients
Requirement.et_extra_props = (
    "Clients MUST always be prepared to deal with additional properties on "
    "instances of any structured type")
Req40.et_extra_props = "4.0 P3 8.1.4 #2; 4.0 P3 9.1.4 #2"

Requirement.et_abstract_no_key_s = (
    "An entity type that is not abstract MUST either contain exactly one "
    "edm:Key element or inherit its key from its base type [not both] (%s)")
Req40.et_abstract_no_key_s = "4.0 P3 8.2 #1 (%s)"

Requirement.et_key_ref_s = (
    "The edm:Key element MUST contain at least one edm:PropertyRef "
    "element (%s)")
Req40.et_key_ref_s = "4.0 P3 8.2 #2 (%s)"

Requirement.key_nullable_s = (
    "The properties that compose the key MUST be non-nullable (%s)")
Req40.key_nullable_s = "4.0 P3 8.2 #3 (%s)"

Requirement.key_type_s = (
    "The properties that compose the key MUST be typed with an enumeration "
    "type or one of the allowed primitive types (%s)")
Req40.key_type_s = "4.0 P3 8.2 #4 (%s)"

# Never tested, this appears to be a constraint on usage
Requirement.key_langunique = (
    "The values of the properties that make up a primary key MUST be "
    "unique across all languages")
Req40.key_langunique = "4.0 P3 8.2 #5"

# Never tested, this appears to be a constraint on usage
Requirement.key_langindepdent = (
    "Entity ids MUST be language independent")
Req40.key_langindepdent = "4.0 P3 8.2 #6"

Requirement.key_name_s = (
    "The edm:PropertyRef element MUST specify a value for the Name "
    "attribute (%s)")
Req40.key_name_s = "4.0 P3 8.3.1 #1 (%s)"

Requirement.key_path_s = (
    "A key property MUST be a primitive property of the entity type itself "
    "or a primitive property of a complex property (%s)")
Req40.key_path_s = "4.0 P3 8.3.1 #2 (%s)"

Requirement.key_alias_s = (
    "If the property identified by the Name attribute is a member of a "
    "complex type, the edm:PropertyRef element MUST specify the Alias "
    "attribute [which must be a SimpleIdentifier] (%s)")
Req40.key_alias_s = "4.0 P3 8.3.2 #1; 4.0 P3 8.3.2 #2 (%s)"

# Never raised, this condition is trapped by Requirement.key_alias_s
Requirement.key_alias_type = (
    "The value of the Alias attribute MUST be a SimpleIdentifier")
Req40.key_alias_type = "4.0 P3 8.3.2 #2"

Requirement.key_alias_unique_s = (
    "The value of the Alias attribute MUST be unique within the set of "
    "aliases, structural and navigation properties of the containing entity "
    "type and any of its base types (%s)")
Req40.key_alias_unique_s = "4.0 P3 8.3.2 #3 (%s)"

Requirement.key_noalias_s = (
    "The Alias attribute MUST NOT be defined if the key property is not a "
    "member of a complex type (%s)")
Req40.key_noalias_s = "4.0 P3 8.3.2 #4 (%s)"

# TODO
Requirement.key_alias_predicate = (
    "For keys that are members of complex types, the alias MUST be used in "
    "the key predicate of URLs instead of the value assigned to the Name "
    "attribute")
Req40.key_alias_predicate = "4.0 P3 8.3.2 #5"

# TODO
Requirement.key_alias_query = (
    "The key alias MUST NOT be used in the query part")
Req40.key_alias_query = "4.0 P3 8.3.2 #6"


# Section 9: Complex Type

# Never raised: covered by Requirement.property_unique_s
Requirement.ct_unique_names = (
    "All properties MUST have a unique name within a complex type")
Req40.key_alias_query = "4.0 P3 9 #1"

Requirement.ct_same_name_s = (
    "Properties MUST NOT have the same name as the declaring complex "
    "type (%s)")
Req40.ct_same_name_s = "4.0 P3 9 #2 (%s)"

Requirement.ct_name = (
    "The edm:ComplexType element MUST include a Name attribute whose "
    "value is a SimpleIdentifier")
Req40.ct_name = "4.0 P3 9.1.1 #1"

# Never raised: identical to Requirement.type_qname_s
Requirement.ct_name_unique_s = (
    "The ComplexType name MUST be unique within its namespace (%s)")
Req40.ct_name_unique_s = "4.0 P3 9.1.1 #2 (%s)"

Requirement.ct_cycle_s = (
    "A complex type MUST NOT introduce an inheritance cycle via the base "
    "type attribute (%s)")
Req40.ct_cycle_s = "4.0 P3 9.1.2 (%s)"

Requirement.ct_open_base_s = (
    "A complex type derived from an open complex type MUST NOT provide a "
    "value of false for the OpenType attribute (%s)")
Req40.ct_open_base_s = "4.0 P3 9.1.4 #1 (%s)"

# Identical to Requirement.et_extra_props
Requirement.ct_extra_props = (
    "Clients MUST always be prepared to deal with additional properties on "
    "instances of any structured type")
Req40.ct_extra_props = "4.0 P3 9.1.4 #2"


# Section 10: Enumeration Type

Requirement.ent_name = (
    "The edm:EnumType element MUST include a Name attribute whose value "
    "is a SimpleIdentifier")
Req40.ent_name = "4.0 P3 10.1.1 #1"

# Never raised: identical to Requirement.type_qname_s
Requirement.ent_name_unique_s = (
    "The EnumType name MUST be unique within its namespace (%s)")
Req40.ent_name_unique_s = "4.0 P3 10.1.1 #2 (%s)"

Requirement.ent_type_s = (
    "The UnderlyingType of an enumeration MUST be one of Edm.Byte, "
    "Edm.SByte, Edm.Int16, Edm.Int32, or Edm.Int64 (%s)")
Req40.ent_type_s = "4.0 P3 10.1.2 (%s)"

Requirement.ent_member_name = (
    "Each edm:Member element MUST include a Name attribute whose value is "
    "a SimpleIdentifier")
Req40.ent_member_name = "4.0 P3 10.2.1 #1"

Requirement.ent_member_unique_s = (
    "The enumeration type MUST NOT declare two members with the same "
    "name (%s)")
Req40.ent_member_unique_s = "4.0 P3 10.2.1 #2 (%s)"

Requirement.ent_auto_value_s = (
    "If the IsFlags attribute has a value of false, either all enumeration "
    "members MUST specify an integer value for the Value attribute, or all "
    "members MUST NOT specify a value for the Value attribute (%s)")
Req40.ent_auto_value_s = "4.0 P3 10.2.2 #1 (%s)"

# Never raised, we do not validate other libraries
Requirement.ent_auto_order = (
    "Client libraries MUST preserve elements in document order")
Req40.ent_auto_order = "4.0 P3 10.2.2 #2"

Requirement.ent_nonauto_value_s = (
    "If the IsFlags attribute has a value of true, a non-negative integer "
    "value MUST be specified for the enumeration member's Value "
    "attribute (%s)")
Req40.ent_nonauto_value_s = "4.0 P3 10.2.2 #3 (%s)"

Requirement.ent_valid_value_s = (
    "The value of an enumeration member MUST be a valid value for the "
    "UnderlyingType of the enumeration type (%s)")
Req40.ent_valid_value_s = "4.0 P3 10.2.2 #4 (%s)"


# Section 11: Type Definition

Requirement.td_name = (
    "The edm:TypeDefinition element MUST include a Name attribute whose "
    "value is a SimpleIdentifier")
Req40.td_name = "4.0 P3 11.1.1 #1"

# Never raised: identical to Requirement.type_qname_s
Requirement.td_name_unique_s = (
    "The TypeDefinition name MUST be unique within its namespace (%s)")
Req40.td_name_unique_s = "4.0 P3 11.1.1 #2 (%s)"

Requirement.td_qname_s = (
    "The edm:TypeDefinition element MUST provide the QualifiedName of a "
    "primitive type as the value of the UnderlyingType attribute (%s)")
Req40.td_qname_s = "4.0 P3 11.1.2 #1 (%s)"

Requirement.td_redef_s = (
    "The underlying type of a type definition MUST NOT be another type "
    "definition (%s)")
Req40.td_redef_s = "4.0 P3 11.1.2 #2 (%s)"

Requirement.td_facet_s = (
    "Facets specified in the type definition MUST NOT be re-specified when "
    "the type definition is used (%s)")
Req40.td_facet_s = "4.0 P3 11.1.3 #1 (%s)"

Requirement.td_annotation_s = (
    "The use of a type definition MUST NOT specify an annotation specified "
    "in the type definition (%s)")
Req40.td_annotation_s = "4.0 P3 11.1.3 #2 (%s)"
