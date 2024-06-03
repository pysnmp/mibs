#
# PySNMP MIB module IEEE8021-PFC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/iee/IEEE8021-PFC-MIB
# Produced by pysmi-1.1.12 at Mon Jun  3 11:53:45 2024
# On host fv-az1385-213 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ieee802dot1mibs, = mibBuilder.importSymbols("IEEE8021-TC-MIB", "ieee802dot1mibs")
ifEntry, ifGeneralInformationGroup = mibBuilder.importSymbols("IF-MIB", "ifEntry", "ifGeneralInformationGroup")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
systemGroup, = mibBuilder.importSymbols("SNMPv2-MIB", "systemGroup")
ObjectIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Unsigned32, Counter32, ModuleIdentity, TimeTicks, iso, NotificationType, Gauge32, IpAddress, MibIdentifier, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Unsigned32", "Counter32", "ModuleIdentity", "TimeTicks", "iso", "NotificationType", "Gauge32", "IpAddress", "MibIdentifier", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ieee8021PFCMib = ModuleIdentity((1, 3, 111, 2, 802, 1, 1, 21))
ieee8021PFCMib.setRevisions(('2018-06-28 00:00', '2014-12-15 00:00', '2010-02-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ieee8021PFCMib.setRevisionsDescriptions(('Published as part of IEEE Std 802.1Q-2018.\n            Cross references updated and corrected.', 'Published as part of IEEE Std 802.1Q 2014 revision.\n            Cross references updated and corrected.', 'Included in IEEE P802.1Qbb\n\n        Copyright (C) IEEE.',))
if mibBuilder.loadTexts: ieee8021PFCMib.setLastUpdated('201806280000Z')
if mibBuilder.loadTexts: ieee8021PFCMib.setOrganization('IEEE 802.1 Working Group')
if mibBuilder.loadTexts: ieee8021PFCMib.setContactInfo('WG-URL:   http://www.ieee802.org/1/\n        WG-EMail: stds-802-1-L@ieee.org \n        Contact:  IEEE 802.1 Working Group Chair\n        Postal:   IEEE Standards Board\n                  445 Hoes Lane\n                  Piscataway, NJ 08854\n                  USA\n        E-mail:   stds-802-1-L@ieee.org\n        ')
if mibBuilder.loadTexts: ieee8021PFCMib.setDescription('Priority-based Flow Control module for IEEE Std 802.1Q.\n\n        Unless otherwise indicated, the references in this MIB\n        module are to IEEE Std 802.1Q.\n\n        Copyright (C) IEEE (2018).\n        This version of this MIB module is part of IEEE Std 802.1Q;\n        see the draft itself for full legal notices.\n      ')
ieee8021PfcMIBObjects = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 21, 1))
ieee8021PfcConformance = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 21, 2))
ieee8021PfcIfTable = MibTable((1, 3, 111, 2, 802, 1, 1, 21, 1, 1), )
if mibBuilder.loadTexts: ieee8021PfcIfTable.setReference('12.23')
if mibBuilder.loadTexts: ieee8021PfcIfTable.setStatus('current')
if mibBuilder.loadTexts: ieee8021PfcIfTable.setDescription('A table of PFC information for all interfaces of a system.')
ieee8021PfcIfEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 21, 1, 1, 1), )
if mibBuilder.loadTexts: ieee8021PfcIfEntry.setReference('12.23')
ifEntry.registerAugmentions(("IEEE8021-PFC-MIB", "ieee8021PfcIfEntry"))
ieee8021PfcIfEntry.setIndexNames(*ifEntry.getIndexNames())
if mibBuilder.loadTexts: ieee8021PfcIfEntry.setStatus('current')
if mibBuilder.loadTexts: ieee8021PfcIfEntry.setDescription('Each entry contains information about\n        the PFC function on a single interface.')
ieee8021PfcLinkDelayAllowance = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 21, 1, 1, 1, 1), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021PfcLinkDelayAllowance.setStatus('current')
if mibBuilder.loadTexts: ieee8021PfcLinkDelayAllowance.setDescription('The allowance made for round-trip propagation delay \n        of the link in bits.\n\n        The value of this object MUST be retained across\n        reinitializations of the management system.')
ieee8021PfcRequests = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 21, 1, 1, 1, 2), Counter32()).setUnits('Requests').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021PfcRequests.setStatus('current')
if mibBuilder.loadTexts: ieee8021PfcRequests.setDescription('A count of the invoked PFC M_CONTROL.request primitives.\n\n         Discontinuities in the value of this counter can occur at\n         re-initialization of the management system, and at other\n         times as indicated by the value of\n         ifCounterDiscontinuityTime.')
ieee8021PfcIndications = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 21, 1, 1, 1, 3), Counter32()).setUnits('Indications').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021PfcIndications.setStatus('current')
if mibBuilder.loadTexts: ieee8021PfcIndications.setDescription('A count of the received PFC M_CONTROL.indication primitives.\n\n         Discontinuities in the value of this counter can occur at\n         re-initialization of the management system, and at other\n         times as indicated by the value of\n         ifCounterDiscontinuityTime.')
ieee8021PfcCompliances = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 21, 2, 1))
ieee8021PfcGroups = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 21, 2, 2))
ieee8021PfcGlobalReqdGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 21, 2, 2, 1)).setObjects(("IEEE8021-PFC-MIB", "ieee8021PfcLinkDelayAllowance"), ("IEEE8021-PFC-MIB", "ieee8021PfcRequests"), ("IEEE8021-PFC-MIB", "ieee8021PfcIndications"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PfcGlobalReqdGroup = ieee8021PfcGlobalReqdGroup.setStatus('current')
if mibBuilder.loadTexts: ieee8021PfcGlobalReqdGroup.setDescription('Objects in the global required group.')
ieee8021PfcCompliance = ModuleCompliance((1, 3, 111, 2, 802, 1, 1, 21, 2, 1, 1)).setObjects(("SNMPv2-MIB", "systemGroup"), ("IF-MIB", "ifGeneralInformationGroup"), ("IEEE8021-PFC-MIB", "ieee8021PfcGlobalReqdGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PfcCompliance = ieee8021PfcCompliance.setStatus('current')
if mibBuilder.loadTexts: ieee8021PfcCompliance.setDescription('The compliance statement for support by a system of\n        the IEEE8021-PFC-MIB module.')
mibBuilder.exportSymbols("IEEE8021-PFC-MIB", ieee8021PfcIndications=ieee8021PfcIndications, ieee8021PfcRequests=ieee8021PfcRequests, ieee8021PfcIfTable=ieee8021PfcIfTable, PYSNMP_MODULE_ID=ieee8021PFCMib, ieee8021PfcCompliances=ieee8021PfcCompliances, ieee8021PfcMIBObjects=ieee8021PfcMIBObjects, ieee8021PfcGroups=ieee8021PfcGroups, ieee8021PfcGlobalReqdGroup=ieee8021PfcGlobalReqdGroup, ieee8021PFCMib=ieee8021PFCMib, ieee8021PfcIfEntry=ieee8021PfcIfEntry, ieee8021PfcCompliance=ieee8021PfcCompliance, ieee8021PfcConformance=ieee8021PfcConformance, ieee8021PfcLinkDelayAllowance=ieee8021PfcLinkDelayAllowance)
