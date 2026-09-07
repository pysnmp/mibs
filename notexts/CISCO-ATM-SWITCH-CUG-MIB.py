#
# PySNMP MIB module CISCO-ATM-SWITCH-CUG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ATM-SWITCH-CUG-MIB
# Source digest sha256:d150b5d69b25d2ae33740bb22ad10c130ee3787e514859b92d53f3931d170486
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "TruthValue")
csCugMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 89))
if mibBuilder.loadTexts: csCugMIB.setLastUpdated('1997-07-07 00:00')
if mibBuilder.loadTexts: csCugMIB.setOrganization('Cisco Systems, Inc.')
class CsCugInterlockCode(TextualConvention, OctetString):
    reference = 'Atm Forum Contribution 96-1347.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(24, 24), )
class Unsigned32(TextualConvention, Gauge32):
    status = 'current'

csCugMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 89, 1))
csCugInterlockCodeTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 89, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: csCugInterlockCodeTable.setStatus('current')
csCugInterlockCodeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 89, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-ATM-SWITCH-CUG-MIB", "csCugInterlockCode"))
if mibBuilder.loadTexts: csCugInterlockCodeEntry.setStatus('current')
csCugInterlockCode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 89, 1, 1, 1, 1), CsCugInterlockCode()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: csCugInterlockCode.setStatus('current')
csCugInterlockCodeAliasName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 89, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 30))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: csCugInterlockCodeAliasName.setStatus('current')
csCugInterlockCodeRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 89, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: csCugInterlockCodeRowStatus.setStatus('current')
csCugIfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 89, 1, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: csCugIfTable.setStatus('current')
csCugIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 89, 1, 2, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: csCugIfEntry.setStatus('current')
csCugIfAccessEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 89, 1, 2, 1, 1), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: csCugIfAccessEnable.setStatus('current')
csCugIfPermitUnknownCugsToUser = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 89, 1, 2, 1, 2), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: csCugIfPermitUnknownCugsToUser.setStatus('current')
csCugIfPermitUnknownCugsFromUser = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 89, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("deny", 1), ("permitPerCall", 2), ("permitPermanently", 3))).clone('deny')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: csCugIfPermitUnknownCugsFromUser.setStatus('current')
csCugIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 89, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: csCugIfRowStatus.setStatus('current')
csCugTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 89, 1, 3), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: csCugTable.setStatus('current')
csCugEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 89, 1, 3, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-ATM-SWITCH-CUG-MIB", "csCugInterlockCode"))
if mibBuilder.loadTexts: csCugEntry.setStatus('current')
csCugIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 89, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: csCugIndex.setStatus('current')
csCugPreferential = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 89, 1, 3, 1, 2), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: csCugPreferential.setStatus('current')
csCugDenySameGroupToUser = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 89, 1, 3, 1, 3), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: csCugDenySameGroupToUser.setStatus('current')
csCugDenySameGroupFromUser = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 89, 1, 3, 1, 4), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: csCugDenySameGroupFromUser.setStatus('current')
csCugRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 89, 1, 3, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: csCugRowStatus.setStatus('current')
csCugMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 89, 3))
csCugMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 89, 3, 1))
csCugMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 89, 3, 2))
csCugMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 89, 3, 1, 1)).setObjects(("CISCO-ATM-SWITCH-CUG-MIB", "csCugMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csCugMIBCompliance = csCugMIBCompliance.setStatus('current')
csCugMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 89, 3, 2, 1)).setObjects(("CISCO-ATM-SWITCH-CUG-MIB", "csCugInterlockCodeAliasName"), ("CISCO-ATM-SWITCH-CUG-MIB", "csCugInterlockCodeRowStatus"), ("CISCO-ATM-SWITCH-CUG-MIB", "csCugIfAccessEnable"), ("CISCO-ATM-SWITCH-CUG-MIB", "csCugIfPermitUnknownCugsToUser"), ("CISCO-ATM-SWITCH-CUG-MIB", "csCugIfPermitUnknownCugsFromUser"), ("CISCO-ATM-SWITCH-CUG-MIB", "csCugIfRowStatus"), ("CISCO-ATM-SWITCH-CUG-MIB", "csCugIndex"), ("CISCO-ATM-SWITCH-CUG-MIB", "csCugPreferential"), ("CISCO-ATM-SWITCH-CUG-MIB", "csCugDenySameGroupToUser"), ("CISCO-ATM-SWITCH-CUG-MIB", "csCugDenySameGroupFromUser"), ("CISCO-ATM-SWITCH-CUG-MIB", "csCugRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csCugMIBGroup = csCugMIBGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-ATM-SWITCH-CUG-MIB", CsCugInterlockCode=CsCugInterlockCode, PYSNMP_MODULE_ID=csCugMIB, Unsigned32=Unsigned32, csCugDenySameGroupFromUser=csCugDenySameGroupFromUser, csCugDenySameGroupToUser=csCugDenySameGroupToUser, csCugEntry=csCugEntry, csCugIfAccessEnable=csCugIfAccessEnable, csCugIfEntry=csCugIfEntry, csCugIfPermitUnknownCugsFromUser=csCugIfPermitUnknownCugsFromUser, csCugIfPermitUnknownCugsToUser=csCugIfPermitUnknownCugsToUser, csCugIfRowStatus=csCugIfRowStatus, csCugIfTable=csCugIfTable, csCugIndex=csCugIndex, csCugInterlockCode=csCugInterlockCode, csCugInterlockCodeAliasName=csCugInterlockCodeAliasName, csCugInterlockCodeEntry=csCugInterlockCodeEntry, csCugInterlockCodeRowStatus=csCugInterlockCodeRowStatus, csCugInterlockCodeTable=csCugInterlockCodeTable, csCugMIB=csCugMIB, csCugMIBCompliance=csCugMIBCompliance, csCugMIBCompliances=csCugMIBCompliances, csCugMIBConformance=csCugMIBConformance, csCugMIBGroup=csCugMIBGroup, csCugMIBGroups=csCugMIBGroups, csCugMIBObjects=csCugMIBObjects, csCugPreferential=csCugPreferential, csCugRowStatus=csCugRowStatus, csCugTable=csCugTable)
