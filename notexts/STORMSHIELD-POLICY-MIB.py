#
# PySNMP MIB module STORMSHIELD-POLICY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/stormshield/STORMSHIELD-POLICY-MIB
# Produced by pysmi-1.1.12 at Tue Dec  3 10:11:46 2024
# On host fv-az575-513 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Counter32, ModuleIdentity, ObjectIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Unsigned32, MibIdentifier, Gauge32, NotificationType, Counter64, iso, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter32", "ModuleIdentity", "ObjectIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Unsigned32", "MibIdentifier", "Gauge32", "NotificationType", "Counter64", "iso", "Integer32")
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
mibBuilder.exportSymbols("STORMSHIELD-POLICY-MIB", snsPolicySync=snsPolicySync, snsPolicySlotName=snsPolicySlotName, snsPolicyTable=snsPolicyTable, snsPolicyName=snsPolicyName, snsPolicyIndex=snsPolicyIndex, snsPolicyActive=snsPolicyActive, snsPolicy=snsPolicy, snsPolicyEntry=snsPolicyEntry, PYSNMP_MODULE_ID=snsPolicy)
