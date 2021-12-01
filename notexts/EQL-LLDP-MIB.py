#
# PySNMP MIB module EQL-LLDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/equallogic/EQL-LLDP-MIB
# Produced by pysmi-1.1.3 at Wed Dec  1 16:28:14 2021
# On host fv-az33-471 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
eqlGroupId, = mibBuilder.importSymbols("EQLGROUP-MIB", "eqlGroupId")
eqlMemberIndex, = mibBuilder.importSymbols("EQLMEMBER-MIB", "eqlMemberIndex")
equalLogic, = mibBuilder.importSymbols("EQUALLOGIC-SMI", "equalLogic")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, iso, enterprises, TimeTicks, Unsigned32, MibIdentifier, ModuleIdentity, Counter32, NotificationType, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Bits, ObjectIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "iso", "enterprises", "TimeTicks", "Unsigned32", "MibIdentifier", "ModuleIdentity", "Counter32", "NotificationType", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Bits", "ObjectIdentity", "Counter64")
TimeInterval, TextualConvention, TruthValue, DisplayString, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TimeInterval", "TextualConvention", "TruthValue", "DisplayString", "MacAddress")
eqlLldpMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 12740, 21))
eqlLldpMib.setRevisions(('2010-07-23 00:00',))
if mibBuilder.loadTexts: eqlLldpMib.setLastUpdated('201503171528Z')
if mibBuilder.loadTexts: eqlLldpMib.setOrganization('EqualLogic Inc.')
eqlLldpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 21, 1))
class EqlLldpV2ChassisIdSubtype(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("chassisComponent", 1), ("interfaceAlias", 2), ("portComponent", 3), ("macAddress", 4), ("networkAddress", 5), ("interfaceName", 6), ("local", 7))

class EqlLldpV2ChassisId(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(255, 255)
    fixedLength = 255

class EqlLldpV2PortIdSubtype(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("interfaceAlias", 1), ("portComponent", 2), ("macAddress", 3), ("networkAddress", 4), ("interfaceName", 5), ("agentCircuitId", 6), ("local", 7))

class EqlLldpV2PortId(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

class EqlLldpV2State(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("off", 0), ("noPeer", 1), ("active", 2), ("multiplePeers", 3))

eqlLldpDynamicIfTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 21, 1, 1), )
if mibBuilder.loadTexts: eqlLldpDynamicIfTable.setStatus('current')
eqlLldpDynamicIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 21, 1, 1, 1), ).setIndexNames((0, "EQLGROUP-MIB", "eqlGroupId"), (0, "EQLMEMBER-MIB", "eqlMemberIndex"), (0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: eqlLldpDynamicIfEntry.setStatus('current')
eqlLldpRemMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 21, 1, 1, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlLldpRemMacAddress.setStatus('current')
eqlLldpV2RemChassisIdSubtype = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 21, 1, 1, 1, 2), EqlLldpV2ChassisIdSubtype()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlLldpV2RemChassisIdSubtype.setStatus('current')
eqlLldpV2RemChassisId = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 21, 1, 1, 1, 3), EqlLldpV2ChassisId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlLldpV2RemChassisId.setStatus('current')
eqlLldpV2RemPortIdSubtype = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 21, 1, 1, 1, 4), EqlLldpV2PortIdSubtype()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlLldpV2RemPortIdSubtype.setStatus('current')
eqlLldpV2RemPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 21, 1, 1, 1, 5), EqlLldpV2PortId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlLldpV2RemPortId.setStatus('current')
eqlLldpV2RemPortDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 21, 1, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlLldpV2RemPortDesc.setStatus('current')
eqlLldpV2RemSysName = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 21, 1, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlLldpV2RemSysName.setStatus('current')
eqlLldpV2RemSysDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 21, 1, 1, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlLldpV2RemSysDesc.setStatus('current')
eqlLldpV2State = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 21, 1, 1, 1, 9), EqlLldpV2State()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlLldpV2State.setStatus('current')
eqlLldpV2RemMgmtAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 21, 1, 1, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlLldpV2RemMgmtAddr.setStatus('current')
mibBuilder.exportSymbols("EQL-LLDP-MIB", eqlLldpV2RemPortDesc=eqlLldpV2RemPortDesc, eqlLldpDynamicIfTable=eqlLldpDynamicIfTable, eqlLldpV2RemPortIdSubtype=eqlLldpV2RemPortIdSubtype, eqlLldpV2RemMgmtAddr=eqlLldpV2RemMgmtAddr, eqlLldpV2RemPortId=eqlLldpV2RemPortId, eqlLldpRemMacAddress=eqlLldpRemMacAddress, eqlLldpV2RemChassisIdSubtype=eqlLldpV2RemChassisIdSubtype, eqlLldpDynamicIfEntry=eqlLldpDynamicIfEntry, eqlLldpMIBObjects=eqlLldpMIBObjects, EqlLldpV2PortIdSubtype=EqlLldpV2PortIdSubtype, EqlLldpV2ChassisId=EqlLldpV2ChassisId, eqlLldpV2RemChassisId=eqlLldpV2RemChassisId, EqlLldpV2PortId=EqlLldpV2PortId, EqlLldpV2State=EqlLldpV2State, eqlLldpV2RemSysDesc=eqlLldpV2RemSysDesc, eqlLldpMib=eqlLldpMib, EqlLldpV2ChassisIdSubtype=EqlLldpV2ChassisIdSubtype, eqlLldpV2RemSysName=eqlLldpV2RemSysName, PYSNMP_MODULE_ID=eqlLldpMib, eqlLldpV2State=eqlLldpV2State)
