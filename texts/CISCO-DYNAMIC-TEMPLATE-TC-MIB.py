#
# PySNMP MIB module CISCO-DYNAMIC-TEMPLATE-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-DYNAMIC-TEMPLATE-TC-MIB
# Source digest sha256:fc5ffa7422195d9d4a332bd46d81cd9a545222faad4eba486c8d0edf4bd6b303
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDynamicTemplateTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 783))
ciscoDynamicTemplateTcMIB.setRevisions(('2007-09-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDynamicTemplateTcMIB.setRevisionsDescriptions(('The initial version of the MIB module.',))
if mibBuilder.loadTexts: ciscoDynamicTemplateTcMIB.setLastUpdated('2012-01-27 00:00')
if mibBuilder.loadTexts: ciscoDynamicTemplateTcMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDynamicTemplateTcMIB.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA 95134\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoDynamicTemplateTcMIB.setDescription('This MIB module defines textual conventions used by the\n        CISCO-DYNAMIC-TEMPLATE-MIB and MIB modules that use and expand\n        on dynamic templates.')
class DynamicTemplateName(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for\n        Describing Simple Network Management Protocol (SNMP)\n        Management\n        Frameworks', RFC-3411, December 2002."
    description = 'A string-value that identifies a dynamic template.  The\n        semantics of the string-value are the same as those specified\n        by the SnmpAdminString textual convention defined by the\n        SNMP-FRAMEWORK-MIB [RFC3411].'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 64)

class DynamicTemplateType(TextualConvention, Integer32):
    description = "An enumerated integer-value describing the type of dynamic\n        template:\n\n        'other'\n            The implementation of the MIB module using this textual\n            convention does not recognize the type of dynamic template.\n\n        'derived'\n            A configuration resulting from the union of the attributes\n            contained by all the dynamic templates associated with a\n            target.  The system generates a derived configuration, and\n            an EMS/NMS cannot directly modify it.  An EMS/NMS can only\n            affect a derived configuration by modifying one or more of\n            the dynamic templates associated with the target.\n\n        'ppp'\n            A PPP template is a set of locally-configured attributes\n            relating to the configuration of a PPP interface.\n\n        'ethernet'\n            An Ethernet template is a set of locally-configured\n            attributes used by the system to configure dynamic\n            interfaces initiated on Ethernet virtual interfaces (e.g.,\n            EoMPLS) or automatically created VLANs.\n\n        'ipSubscriber'\n            An IP subscriber template is a set of locally-configured\n            attributes used by the system to configure certain types of\n            IP and L2 subscriber sessions.\n\n        'service'\n            A service template is a set of locally-configured attributes\n            used by the system to configure subscriber sessions.  These\n            attributes specifically relate to services, and the system\n            applies these attributes in response to subscriber session\n            life-cycle events."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 1), ("derived", 2), ("ppp", 3), ("ethernet", 4), ("ipSubscriber", 5), ("service", 6))

class DynamicTemplateTargetType(TextualConvention, Integer32):
    reference = "K. McCloghrie and F. Kastenholtz, 'The Interfaces Group\n        MIB',\n        RFC-2863, June 2000."
    description = "An enumerated integer-value describing the type of target\n        associated with one or more dynamic templates:\n\n            'other'\n                The implementation of the MIB module using this textual\n                convention does not recognize the type of target.\n\n            'interface'\n                The target is a physical, logical, or virtual interface\n                represented by an ifEntry (defined by the IF-MIB).\n\n        An implementation must ensure that DynamicTemplateTargetType\n        object and any associated DynamicTemplateTargetId objects are\n        consistent.  An attempt to set a DynamicTemplateTargetType\n        object to a value inconsistent with the associated\n        DynamicTemplateTargetId object must result in a response with\n        an\n        error-status of 'inconsistentValue'."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("other", 1), ("interface", 2))

class DynamicTemplateTargetId(TextualConvention, OctetString):
    reference = "K. McCloghrie and F. Kastenholtz, 'The Interfaces Group\n        MIB',\n        RFC-2863, June 2000."
    description = "An binary string-value in network byte order identifying a\n        target associated with one or more dynamic templates.\n\n        An implementation must interpret a DynamicTemplateTargetId\n        value\n        within the context of a DynamicTemplateTargetType.  Every usage\n        of the DynamicTemplateTargetId textual convention must have a\n        corresponding object specifying the DynamicTemplateType that\n        provides this context.  It is most appropriate that a MIB\n        module\n        logical registers the DynamicTemplateType object before the use\n        of the DynamicTemplateTargetId textual convention within the\n        same logical row.\n\n        The value of a DynamicTemplateTargetId object must always be\n        consistent with the value of the associated\n        DynamicTemplateTargetType object.  An attempt to set a\n        DynamicTemplateTargetId object to a value inconsistent with the\n        with the associated DynamicTemplateTargetType object must\n        result\n        in a response with an error-status of 'inconsistentValue'.\n\n        If the DynamicTemplateTargetType is 'interface', then the representation\n        of DynamicTemplateTargetId is as below\n\n        octets   contents              encoding\n         1-4     ifIndex               network-byte order"
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 20)

mibBuilder.exportSymbols("CISCO-DYNAMIC-TEMPLATE-TC-MIB", DynamicTemplateName=DynamicTemplateName, DynamicTemplateTargetId=DynamicTemplateTargetId, DynamicTemplateTargetType=DynamicTemplateTargetType, DynamicTemplateType=DynamicTemplateType, PYSNMP_MODULE_ID=ciscoDynamicTemplateTcMIB, ciscoDynamicTemplateTcMIB=ciscoDynamicTemplateTcMIB)
