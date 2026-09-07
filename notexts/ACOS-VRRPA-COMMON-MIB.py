#
# PySNMP MIB module ACOS-VRRPA-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source ACOS-VRRPA-COMMON-MIB
# Source digest sha256:24921de816559a0514bba105066f535c801a6f168405adb2089873fe5b7a0907
# Produced by pysmi-2.3.0
#
acosSchema, = mibBuilder.importSymbols("A10-AX-MIB", "acosSchema")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, PhysAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "PhysAddress", "TextualConvention")
vrrpACommonModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 6))
if mibBuilder.loadTexts: vrrpACommonModule.setLastUpdated('2007-05-07 13:27')
if mibBuilder.loadTexts: vrrpACommonModule.setOrganization('A10 Networks, Inc.')
common = MibIdentifier((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 6, 1))
commonStatsTable = MibTable((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 6, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: commonStatsTable.setStatus('current')
commonStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 6, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ACOS-VRRPA-COMMON-MIB", "commonStatsSlotId"))
if mibBuilder.loadTexts: commonStatsEntry.setStatus('current')
commonStatsSlotId = MibTableColumn((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 6, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: commonStatsSlotId.setStatus('current')
commonStatsVrrpCommonDummy = MibTableColumn((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 6, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: commonStatsVrrpCommonDummy.setStatus('current')
mibBuilder.exportSymbols("ACOS-VRRPA-COMMON-MIB", PYSNMP_MODULE_ID=vrrpACommonModule, common=common, commonStatsEntry=commonStatsEntry, commonStatsSlotId=commonStatsSlotId, commonStatsTable=commonStatsTable, commonStatsVrrpCommonDummy=commonStatsVrrpCommonDummy, vrrpACommonModule=vrrpACommonModule)
