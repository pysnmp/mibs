#
# PySNMP MIB module PRVT-LLDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binos/PRVT-LLDP-MIB
# Produced by pysmi-1.1.8 at Thu Jan  6 19:50:43 2022
# On host fv-az121-779 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
switch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "switch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, MibIdentifier, Counter32, NotificationType, TimeTicks, ModuleIdentity, Integer32, Gauge32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibIdentifier", "Counter32", "NotificationType", "TimeTicks", "ModuleIdentity", "Integer32", "Gauge32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Bits", "IpAddress")
TextualConvention, RowStatus, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "TruthValue", "DisplayString")
prvtLldpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 1, 5, 145))
prvtLldpMIB.setRevisions(('2009-07-28 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: prvtLldpMIB.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: prvtLldpMIB.setLastUpdated('200907280000Z')
if mibBuilder.loadTexts: prvtLldpMIB.setOrganization('BATM Advanced Communication')
if mibBuilder.loadTexts: prvtLldpMIB.setContactInfo('BATM/Telco Systems Support team\n            Email: \n            For North America: techsupport@telco.com\n            For North Europe: support@batm.de, info@batm.de\n            For the rest of the world: techsupport@telco.com')
if mibBuilder.loadTexts: prvtLldpMIB.setDescription('Management Information Base module for LLDP configuration')
prvtLldpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 145, 0))
prvtLldpEnable = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 145, 0, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtLldpEnable.setStatus('current')
if mibBuilder.loadTexts: prvtLldpEnable.setDescription('Enable/disable the LLDP on the device')
mibBuilder.exportSymbols("PRVT-LLDP-MIB", prvtLldpEnable=prvtLldpEnable, prvtLldpMIB=prvtLldpMIB, PYSNMP_MODULE_ID=prvtLldpMIB, prvtLldpObjects=prvtLldpObjects)
