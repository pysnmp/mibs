#
# PySNMP MIB module STORMSHIELD-POLICY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/stormshield/STORMSHIELD-POLICY-MIB
# Produced by pysmi-1.1.8 at Thu Sep  7 10:23:20 2023
# On host fv-az627-713 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Counter32, Gauge32, NotificationType, iso, ModuleIdentity, TimeTicks, IpAddress, ObjectIdentity, Integer32, Bits, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter32", "Gauge32", "NotificationType", "iso", "ModuleIdentity", "TimeTicks", "IpAddress", "ObjectIdentity", "Integer32", "Bits", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
stormshieldMIB, = mibBuilder.importSymbols("STORMSHIELD-SMI-MIB", "stormshieldMIB")
snsPolicy = ModuleIdentity((1, 3, 6, 1, 4, 1, 11256, 1, 8))
snsPolicy.setRevisions(('2017-02-20 00:00',))
if mibBuilder.loadTexts: snsPolicy.setLastUpdated('201702200000Z')
if mibBuilder.loadTexts: snsPolicy.setOrganization('Stormshield')
snsPolicyTable = MibTable((1, 3, 6, 1, 4, 1, 11256, 1, 8, 1), )
if mibBuilder.loadTexts: snsPolicyTable.setStatus('current')
snsPolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11256, 1, 8, 1, 1), ).setIndexNames((0, "STORMSHIELD-POLICY-MIB", "snsPolicyIndex"))
if mibBuilder.loadTexts: snsPolicyEntry.setStatus('current')
snsPolicyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 8, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsPolicyIndex.setStatus('current')
snsPolicyName = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 8, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsPolicyName.setStatus('current')
snsPolicySlotName = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 8, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsPolicySlotName.setStatus('current')
snsPolicyActive = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 8, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsPolicyActive.setStatus('current')
snsPolicySync = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 8, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsPolicySync.setStatus('current')
mibBuilder.exportSymbols("STORMSHIELD-POLICY-MIB", snsPolicyTable=snsPolicyTable, snsPolicyIndex=snsPolicyIndex, snsPolicyActive=snsPolicyActive, snsPolicySync=snsPolicySync, snsPolicyEntry=snsPolicyEntry, snsPolicyName=snsPolicyName, PYSNMP_MODULE_ID=snsPolicy, snsPolicySlotName=snsPolicySlotName, snsPolicy=snsPolicy)
