#
# PySNMP MIB module PRVT-LLDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binos/PRVT-LLDP-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 15:09:44 2021
# On host fv-az36-794 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
switch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "switch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, NotificationType, IpAddress, MibIdentifier, ObjectIdentity, ModuleIdentity, Gauge32, Unsigned32, TimeTicks, Integer32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "NotificationType", "IpAddress", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "Gauge32", "Unsigned32", "TimeTicks", "Integer32", "Bits")
TruthValue, TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString", "RowStatus")
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
mibBuilder.exportSymbols("PRVT-LLDP-MIB", prvtLldpMIB=prvtLldpMIB, PYSNMP_MODULE_ID=prvtLldpMIB, prvtLldpEnable=prvtLldpEnable, prvtLldpObjects=prvtLldpObjects)
