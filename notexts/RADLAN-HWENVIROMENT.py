#
# PySNMP MIB module RADLAN-HWENVIROMENT (http://snmplabs.com/pysmi)
# ASN.1 source https://pysnmp.github.io:443/mibs/asn1/RADLAN-HWENVIROMENT
# Produced by pysmi-1.1.10 at Thu Oct 26 13:05:43 2023
# On host fv-az247-868 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, iso, IpAddress, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, ModuleIdentity, Bits, TimeTicks, Counter64, MibIdentifier, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "iso", "IpAddress", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "ModuleIdentity", "Bits", "TimeTicks", "Counter64", "MibIdentifier", "Unsigned32", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
DisplayString, = mibBuilder.importSymbols("SNMPv2-TC-v1", "DisplayString")
rlEnv = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 83))
rlEnv.setRevisions(('2003-09-21 00:00',))
if mibBuilder.loadTexts: rlEnv.setLastUpdated('200309210000Z')
if mibBuilder.loadTexts: rlEnv.setOrganization('Radlan Computer Communications Ltd.')
class RlEnvMonState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("normal", 1), ("warning", 2), ("critical", 3), ("shutdown", 4), ("notPresent", 5), ("notFunctioning", 6))

rlEnvPhysicalDescription = MibIdentifier((1, 3, 6, 1, 4, 1, 89, 83, 1))
rlEnvMonFanStatusTable = MibTable((1, 3, 6, 1, 4, 1, 89, 83, 1, 1), )
if mibBuilder.loadTexts: rlEnvMonFanStatusTable.setStatus('current')
rlEnvMonFanStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 83, 1, 1, 1), ).setIndexNames((0, "RADLAN-HWENVIROMENT", "rlEnvMonFanStatusIndex"))
if mibBuilder.loadTexts: rlEnvMonFanStatusEntry.setStatus('current')
rlEnvMonFanStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 83, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: rlEnvMonFanStatusIndex.setStatus('current')
rlEnvMonFanStatusDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 83, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlEnvMonFanStatusDescr.setStatus('current')
rlEnvMonFanState = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 83, 1, 1, 1, 3), RlEnvMonState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlEnvMonFanState.setStatus('current')
rlEnvMonSupplyStatusTable = MibTable((1, 3, 6, 1, 4, 1, 89, 83, 1, 2), )
if mibBuilder.loadTexts: rlEnvMonSupplyStatusTable.setStatus('current')
rlEnvMonSupplyStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 83, 1, 2, 1), ).setIndexNames((0, "RADLAN-HWENVIROMENT", "rlEnvMonSupplyStatusIndex"))
if mibBuilder.loadTexts: rlEnvMonSupplyStatusEntry.setStatus('current')
rlEnvMonSupplyStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 83, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: rlEnvMonSupplyStatusIndex.setStatus('current')
rlEnvMonSupplyStatusDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 83, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlEnvMonSupplyStatusDescr.setStatus('current')
rlEnvMonSupplyState = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 83, 1, 2, 1, 3), RlEnvMonState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlEnvMonSupplyState.setStatus('current')
rlEnvMonSupplySource = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 83, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("ac", 2), ("dc", 3), ("externalPowerSupply", 4), ("internalRedundant", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlEnvMonSupplySource.setStatus('current')
mibBuilder.exportSymbols("RADLAN-HWENVIROMENT", rlEnv=rlEnv, RlEnvMonState=RlEnvMonState, rlEnvMonFanState=rlEnvMonFanState, rlEnvMonSupplyState=rlEnvMonSupplyState, rlEnvMonFanStatusIndex=rlEnvMonFanStatusIndex, rlEnvMonSupplyStatusDescr=rlEnvMonSupplyStatusDescr, rlEnvMonFanStatusTable=rlEnvMonFanStatusTable, rlEnvMonFanStatusDescr=rlEnvMonFanStatusDescr, rlEnvMonFanStatusEntry=rlEnvMonFanStatusEntry, rlEnvMonSupplyStatusIndex=rlEnvMonSupplyStatusIndex, rlEnvPhysicalDescription=rlEnvPhysicalDescription, PYSNMP_MODULE_ID=rlEnv, rlEnvMonSupplyStatusTable=rlEnvMonSupplyStatusTable, rlEnvMonSupplySource=rlEnvMonSupplySource, rlEnvMonSupplyStatusEntry=rlEnvMonSupplyStatusEntry)
