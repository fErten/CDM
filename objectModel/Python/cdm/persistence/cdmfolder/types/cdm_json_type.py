from typing import Union

from .argument import Argument
from .attribute_context import AttributeContext
from .attribute_group import AttributeGroup
from .attribute_group_reference import AttributeGroupReference
from .cdm_import import Import
from .constant_entity import ConstantEntity
from .data_partition import DataPartition
from .data_partition_pattern import DataPartitionPattern
from .data_type import DataType
from .data_type_reference import DataTypeReference
from .document_content import DocumentContent
from .entity import Entity
from .entity_attribute import EntityAttribute
from .entity_reference import EntityReference
from .folder import Folder
from .local_entity_declaration import LocalEntityDeclaration
from .manifest_declaration import ManifestDeclaration
from .parameter import Parameter
from .purpose import Purpose
from .purpose_reference import PurposeReference
from .referenced_entity_declaration import ReferencedEntityDeclaration
from .trait import Trait
from .trait_reference import TraitReference
from .type_attribute import TypeAttribute

CdmJsonType = Union[
    str,
    object,
    Argument,
    AttributeContext,
    AttributeGroup,
    AttributeGroupReference,
    ConstantEntity,
    DataPartition,
    DataPartitionPattern,
    DataType,
    DataTypeReference,
    DocumentContent,
    Entity,
    EntityAttribute,
    EntityReference,
    Folder,
    Import,
    LocalEntityDeclaration,
    ManifestDeclaration,
    Parameter,
    Purpose,
    PurposeReference,
    ReferencedEntityDeclaration,
    Trait,
    TraitReference,
    TypeAttribute
]
