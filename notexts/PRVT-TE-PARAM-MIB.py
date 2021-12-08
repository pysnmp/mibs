#
# PySNMP MIB module PRVT-TE-PARAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binox/PRVT-TE-PARAM-MIB
# Produced by pysmi-1.1.3 at Wed Dec  8 18:20:48 2021
# On host fv-az74-115 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
mpls, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "mpls")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, ModuleIdentity, Counter64, Gauge32, ObjectIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, MibIdentifier, TimeTicks, Integer32, Counter32, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "MibIdentifier", "TimeTicks", "Integer32", "Counter32", "Bits", "Unsigned32")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
prvtTeParamMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 9))
prvtTeParamMIB.setRevisions(('2010-04-28 00:00',))
if mibBuilder.loadTexts: prvtTeParamMIB.setLastUpdated('201004280000Z')
if mibBuilder.loadTexts: prvtTeParamMIB.setOrganization('BATM Advanced Communication')
class PrvtTeLinkBandwidthSpeed(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'

class PrvtTeLinkBandwidthUnits(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("bps", 0), ("kbps", 1), ("mbps", 2), ("gbps", 3))

prvtTeParamMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 9, 1))
prvtTeParamLinkTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 9, 1, 2), )
if mibBuilder.loadTexts: prvtTeParamLinkTable.setStatus('current')
prvtTeParamLinkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 9, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: prvtTeParamLinkEntry.setStatus('current')
prvtTeParamLinkRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 9, 1, 2, 1, 1), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtTeParamLinkRowStatus.setStatus('current')
prvtTeParamLinkMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 9, 1, 2, 1, 2), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtTeParamLinkMetric.setStatus('current')
prvtTeParamLinkPhyBandwidthSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 9, 1, 2, 1, 3), PrvtTeLinkBandwidthSpeed()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtTeParamLinkPhyBandwidthSpeed.setStatus('current')
prvtTeParamLinkPhyBandwidthUnits = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 9, 1, 2, 1, 4), PrvtTeLinkBandwidthUnits()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtTeParamLinkPhyBandwidthUnits.setStatus('current')
prvtTeParamLinkMaxRsvBwSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 9, 1, 2, 1, 5), PrvtTeLinkBandwidthSpeed()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtTeParamLinkMaxRsvBwSpeed.setStatus('current')
prvtTeParamLinkMaxRsvBwUnits = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 9, 1, 2, 1, 6), PrvtTeLinkBandwidthUnits()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtTeParamLinkMaxRsvBwUnits.setStatus('current')
prvtTeParamLinkAdminGrpTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 9, 1, 3), )
if mibBuilder.loadTexts: prvtTeParamLinkAdminGrpTable.setStatus('current')
prvtTeParamLinkAdminGrpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 9, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "PRVT-TE-PARAM-MIB", "prvtTeParamLinkAdminGrpId"))
if mibBuilder.loadTexts: prvtTeParamLinkAdminGrpEntry.setStatus('current')
prvtTeParamLinkAdminGrpId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 9, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32)))
if mibBuilder.loadTexts: prvtTeParamLinkAdminGrpId.setStatus('current')
prvtTeParamLinkAdminGrpRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 9, 1, 3, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtTeParamLinkAdminGrpRowStatus.setStatus('current')
prvtTeParamAdminGroupTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 9, 1, 5), )
if mibBuilder.loadTexts: prvtTeParamAdminGroupTable.setStatus('current')
prvtTeParamAdminGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 9, 1, 5, 1), ).setIndexNames((0, "PRVT-TE-PARAM-MIB", "prvtTeParamAdminGroupId"))
if mibBuilder.loadTexts: prvtTeParamAdminGroupEntry.setStatus('current')
prvtTeParamAdminGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 9, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32)))
if mibBuilder.loadTexts: prvtTeParamAdminGroupId.setStatus('current')
prvtTeParamAdminGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 9, 1, 5, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtTeParamAdminGroupRowStatus.setStatus('current')
prvtTeParamAdminGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 9, 1, 5, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 15))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtTeParamAdminGroupName.setStatus('current')
mibBuilder.exportSymbols("PRVT-TE-PARAM-MIB", prvtTeParamLinkRowStatus=prvtTeParamLinkRowStatus, prvtTeParamLinkTable=prvtTeParamLinkTable, prvtTeParamLinkMetric=prvtTeParamLinkMetric, prvtTeParamLinkAdminGrpRowStatus=prvtTeParamLinkAdminGrpRowStatus, prvtTeParamLinkAdminGrpId=prvtTeParamLinkAdminGrpId, prvtTeParamLinkAdminGrpTable=prvtTeParamLinkAdminGrpTable, prvtTeParamAdminGroupTable=prvtTeParamAdminGroupTable, prvtTeParamLinkPhyBandwidthUnits=prvtTeParamLinkPhyBandwidthUnits, prvtTeParamMIB=prvtTeParamMIB, prvtTeParamAdminGroupName=prvtTeParamAdminGroupName, prvtTeParamAdminGroupRowStatus=prvtTeParamAdminGroupRowStatus, prvtTeParamMIBObjects=prvtTeParamMIBObjects, prvtTeParamLinkPhyBandwidthSpeed=prvtTeParamLinkPhyBandwidthSpeed, prvtTeParamLinkMaxRsvBwUnits=prvtTeParamLinkMaxRsvBwUnits, PrvtTeLinkBandwidthSpeed=PrvtTeLinkBandwidthSpeed, prvtTeParamLinkMaxRsvBwSpeed=prvtTeParamLinkMaxRsvBwSpeed, PYSNMP_MODULE_ID=prvtTeParamMIB, prvtTeParamLinkEntry=prvtTeParamLinkEntry, prvtTeParamAdminGroupId=prvtTeParamAdminGroupId, prvtTeParamAdminGroupEntry=prvtTeParamAdminGroupEntry, prvtTeParamLinkAdminGrpEntry=prvtTeParamLinkAdminGrpEntry, PrvtTeLinkBandwidthUnits=PrvtTeLinkBandwidthUnits)
