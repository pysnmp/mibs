#
# PySNMP MIB module STORMSHIELD-POLICY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/stormshield/STORMSHIELD-POLICY-MIB
# Produced by pysmi-1.1.3 at Wed Dec  8 18:06:09 2021
# On host fv-az74-115 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Gauge32, Unsigned32, ModuleIdentity, Counter64, Bits, Integer32, IpAddress, Counter32, iso, TimeTicks, NotificationType, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Gauge32", "Unsigned32", "ModuleIdentity", "Counter64", "Bits", "Integer32", "IpAddress", "Counter32", "iso", "TimeTicks", "NotificationType", "MibIdentifier")
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
mibBuilder.exportSymbols("STORMSHIELD-POLICY-MIB", snsPolicySync=snsPolicySync, PYSNMP_MODULE_ID=snsPolicy, snsPolicyEntry=snsPolicyEntry, snsPolicyActive=snsPolicyActive, snsPolicyIndex=snsPolicyIndex, snsPolicyTable=snsPolicyTable, snsPolicySlotName=snsPolicySlotName, snsPolicy=snsPolicy, snsPolicyName=snsPolicyName)
