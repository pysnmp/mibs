#
# PySNMP MIB module IEEE8021-MVRPX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/iee/IEEE8021-MVRPX-MIB
# Produced by pysmi-1.1.12 at Mon Sep  9 10:58:22 2024
# On host fv-az1245-503 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.14 (main, Jul 16 2024, 19:03:10) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ieee8021BridgeBasePortEntry, = mibBuilder.importSymbols("IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortEntry")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
systemGroup, = mibBuilder.importSymbols("SNMPv2-MIB", "systemGroup")
NotificationType, TimeTicks, Counter32, Integer32, Bits, Unsigned32, MibIdentifier, ObjectIdentity, iso, Gauge32, IpAddress, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "Counter32", "Integer32", "Bits", "Unsigned32", "MibIdentifier", "ObjectIdentity", "iso", "Gauge32", "IpAddress", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
ieee8021MvrpxMib = ModuleIdentity((1, 3, 111, 2, 802, 1, 1, 22))
ieee8021MvrpxMib.setRevisions(('2018-06-28 00:00', '2014-12-15 00:00', '2011-04-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ieee8021MvrpxMib.setRevisionsDescriptions(('Published as part of IEEE Std 802.1Q-2018.\n            Cross references updated and corrected.', 'Published as part of IEEE Std 802.1Q 2014 revision.\n            Cross references updated and corrected.', 'Included in IEEE Std 802.1Qbe-2011\n\n        Copyright (C) IEEE (2011).',))
if mibBuilder.loadTexts: ieee8021MvrpxMib.setLastUpdated('201806280000Z')
if mibBuilder.loadTexts: ieee8021MvrpxMib.setOrganization('IEEE 802.1 Working Group')
if mibBuilder.loadTexts: ieee8021MvrpxMib.setContactInfo('WG-URL:   http://www.ieee802.org/1/\n        WG-EMail: stds-802-1-L@ieee.org \n        Contact:  IEEE 802.1 Working Group Chair\n        Postal:   IEEE Standards Board\n                  445 Hoes Lane\n                  Piscataway, NJ 08854\n                  USA\n        E-mail:   stds-802-1-L@ieee.org\n       ')
if mibBuilder.loadTexts: ieee8021MvrpxMib.setDescription('Multiple VLAN Registration Protocol extension module for\n        managing MVRP extensions defined in IEEE Std 802.1Q\n\n        Unless otherwise indicated, the references in this MIB\n        module are to IEEE Std 802.1Q.\n\n        Copyright (C) IEEE (2018).\n        This version of this MIB module is part of IEEE Std 802.1Q;\n        see the draft itself for full legal notices.\n       ')
ieee8021MvrpxMIBObjects = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 22, 1))
ieee8021MvrpxConformance = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 22, 2))
ieee8021MvrpxPortTable = MibTable((1, 3, 111, 2, 802, 1, 1, 22, 1, 1), )
if mibBuilder.loadTexts: ieee8021MvrpxPortTable.setReference('12.9.2')
if mibBuilder.loadTexts: ieee8021MvrpxPortTable.setStatus('current')
if mibBuilder.loadTexts: ieee8021MvrpxPortTable.setDescription('A table that contains controls for the Multiple VLAN\n        Registration Protocol (MVRP) state machines for all of the Ports\n        of a Bridge.')
ieee8021MvrpxPortEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 22, 1, 1, 1), )
ieee8021BridgeBasePortEntry.registerAugmentions(("IEEE8021-MVRPX-MIB", "ieee8021MvrpxPortEntry"))
ieee8021MvrpxPortEntry.setIndexNames(*ieee8021BridgeBasePortEntry.getIndexNames())
if mibBuilder.loadTexts: ieee8021MvrpxPortEntry.setStatus('current')
if mibBuilder.loadTexts: ieee8021MvrpxPortEntry.setDescription('Each entry contains the MVRP Registrar controls for one Port.')
ieee8021MvrpxPortNewOnly = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 22, 1, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021MvrpxPortNewOnly.setReference('12.9.2.1.3, 12.9.2.2.2')
if mibBuilder.loadTexts: ieee8021MvrpxPortNewOnly.setStatus('current')
if mibBuilder.loadTexts: ieee8021MvrpxPortNewOnly.setDescription('The mode of operation of the MVRP state machines on\n        this port, if enabled.  The value of this object and the value\n        of the individual Port+Attribute type enable object\n        ieee8021QBridgePortMvrpEnabledStatus combine to control the\n        state machines as follows:\n\n        ieee8021MvrpxPortNewOnly\n                            ieee8021QBridgePortMvrpEnabledStatus\n                                            MVRP state machines\n\n        not implemented     true(1)         Full participant\n        false(2)            true(1)         Full participant\n        true(1)             true(1)         New-only participant\n        not implemented     false(2)        MVRP disabled\n        false(2)            false(2)        MVRP disabled\n        true(1)             false(2)        MVRP disabled\n\n        This object affects all MVRP Applicant and Registrar state\n        machines on this port. A change to the value of this object\n        will cause a reset of all MVRP state machines for this attribute\n        type on this port.\n\n        The value of this object MUST be retained across\n        reinitializations of the management system.')
ieee8021MvrpxPortMvrpNewPropagated = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 22, 1, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021MvrpxPortMvrpNewPropagated.setReference('12.7.7.1.2:d, 12.7.7.3.3:d')
if mibBuilder.loadTexts: ieee8021MvrpxPortMvrpNewPropagated.setStatus('current')
if mibBuilder.loadTexts: ieee8021MvrpxPortMvrpNewPropagated.setDescription('The mode of operation of the MVRP on this port, if enabled.\n        If this object contains the value true(1), then all Static VLAN\n        Registration Entries that are Registration Fixed are treated as\n        Registration Fixed (New propagated), and if false(2), as\n        Registration Fixed (New ignored)\n\n        This object affects only the MVRP Applicant and Registrar state\n        machines on this port. A change to the value of this object\n        will cause a reset of all MVRP state machines on this port.\n\n        The value of this object MUST be retained across\n        reinitializations of the management system.')
ieee8021MvrpxPortXmitZero = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 22, 1, 1, 1, 3), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021MvrpxPortXmitZero.setReference('12.9.2.1.3:c, 12.9.2.2.2:e, 11.2.3.1.7')
if mibBuilder.loadTexts: ieee8021MvrpxPortXmitZero.setStatus('current')
if mibBuilder.loadTexts: ieee8021MvrpxPortXmitZero.setDescription('Selects whether MVRP is enabled to transmit 0 as the attribute\n        value for the one VLAN ID for which this Port is in the untagged\n        set, true(1) to enable transmit 0, and false(2) to transmit the\n        VLAN ID.  The value 0 is not transmitted unless\n        ieee8021MvrpxPortNewOnly is true(1).\n\n        This feature is optional.  If not supported, the system SHALL\n        NOT allow this object to be set to the value true(1).\n\n        The value of this object MUST be retained across\n        reinitializations of the management system.')
ieee8021MvrpxCompliances = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 22, 2, 1))
ieee8021MvrpxGroups = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 22, 2, 2))
ieee8021MvrpxReqdGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 22, 2, 2, 1)).setObjects(("IEEE8021-MVRPX-MIB", "ieee8021MvrpxPortNewOnly"), ("IEEE8021-MVRPX-MIB", "ieee8021MvrpxPortMvrpNewPropagated"), ("IEEE8021-MVRPX-MIB", "ieee8021MvrpxPortXmitZero"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021MvrpxReqdGroup = ieee8021MvrpxReqdGroup.setStatus('current')
if mibBuilder.loadTexts: ieee8021MvrpxReqdGroup.setDescription('Objects in the MVRP extension augmentation table required\n        group.')
ieee8021MvrpxCompliance = ModuleCompliance((1, 3, 111, 2, 802, 1, 1, 22, 2, 1, 1)).setObjects(("SNMPv2-MIB", "systemGroup"), ("IEEE8021-MVRPX-MIB", "ieee8021MvrpxReqdGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021MvrpxCompliance = ieee8021MvrpxCompliance.setStatus('current')
if mibBuilder.loadTexts: ieee8021MvrpxCompliance.setDescription('The compliance statement for support by a Bridge of\n        the IEEE8021-MVRPX-MIB module.')
mibBuilder.exportSymbols("IEEE8021-MVRPX-MIB", PYSNMP_MODULE_ID=ieee8021MvrpxMib, ieee8021MvrpxCompliance=ieee8021MvrpxCompliance, ieee8021MvrpxMIBObjects=ieee8021MvrpxMIBObjects, ieee8021MvrpxCompliances=ieee8021MvrpxCompliances, ieee8021MvrpxPortMvrpNewPropagated=ieee8021MvrpxPortMvrpNewPropagated, ieee8021MvrpxGroups=ieee8021MvrpxGroups, ieee8021MvrpxPortXmitZero=ieee8021MvrpxPortXmitZero, ieee8021MvrpxReqdGroup=ieee8021MvrpxReqdGroup, ieee8021MvrpxMib=ieee8021MvrpxMib, ieee8021MvrpxPortNewOnly=ieee8021MvrpxPortNewOnly, ieee8021MvrpxConformance=ieee8021MvrpxConformance, ieee8021MvrpxPortEntry=ieee8021MvrpxPortEntry, ieee8021MvrpxPortTable=ieee8021MvrpxPortTable)
