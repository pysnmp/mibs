#
# PySNMP MIB module RADLAN-HWENVIROMENT (http://snmplabs.com/pysmi)
# ASN.1 source https://pysnmp.github.io:443/mibs/asn1/RADLAN-HWENVIROMENT
# Produced by pysmi-1.1.8 at Sat Jan 15 05:21:48 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, IpAddress, TimeTicks, Counter32, NotificationType, Gauge32, iso, Counter64, Unsigned32, ObjectIdentity, Bits, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "IpAddress", "TimeTicks", "Counter32", "NotificationType", "Gauge32", "iso", "Counter64", "Unsigned32", "ObjectIdentity", "Bits", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("RADLAN-HWENVIROMENT", rlEnvPhysicalDescription=rlEnvPhysicalDescription, rlEnvMonFanStatusDescr=rlEnvMonFanStatusDescr, rlEnvMonSupplyStatusTable=rlEnvMonSupplyStatusTable, rlEnv=rlEnv, rlEnvMonSupplySource=rlEnvMonSupplySource, rlEnvMonSupplyStatusDescr=rlEnvMonSupplyStatusDescr, rlEnvMonFanStatusEntry=rlEnvMonFanStatusEntry, RlEnvMonState=RlEnvMonState, rlEnvMonSupplyStatusIndex=rlEnvMonSupplyStatusIndex, rlEnvMonSupplyState=rlEnvMonSupplyState, PYSNMP_MODULE_ID=rlEnv, rlEnvMonFanStatusIndex=rlEnvMonFanStatusIndex, rlEnvMonSupplyStatusEntry=rlEnvMonSupplyStatusEntry, rlEnvMonFanState=rlEnvMonFanState, rlEnvMonFanStatusTable=rlEnvMonFanStatusTable)
