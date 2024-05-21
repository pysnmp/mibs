#
# PySNMP MIB module STORMSHIELD-POLICY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/stormshield/STORMSHIELD-POLICY-MIB
# Produced by pysmi-1.1.12 at Tue May 21 07:01:19 2024
# On host fv-az1501-253 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, iso, Unsigned32, Bits, MibIdentifier, TimeTicks, Counter32, Integer32, Gauge32, IpAddress, ModuleIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "iso", "Unsigned32", "Bits", "MibIdentifier", "TimeTicks", "Counter32", "Integer32", "Gauge32", "IpAddress", "ModuleIdentity", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("STORMSHIELD-POLICY-MIB", snsPolicyIndex=snsPolicyIndex, snsPolicyEntry=snsPolicyEntry, snsPolicySync=snsPolicySync, snsPolicyActive=snsPolicyActive, snsPolicySlotName=snsPolicySlotName, snsPolicyTable=snsPolicyTable, snsPolicyName=snsPolicyName, PYSNMP_MODULE_ID=snsPolicy, snsPolicy=snsPolicy)
