#
# PySNMP MIB module PRVT-TE-PARAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binox/PRVT-TE-PARAM-MIB
# Produced by pysmi-1.1.3 at Thu Dec  9 15:31:39 2021
# On host fv-az39-899 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
mpls, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "mpls")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, TimeTicks, ObjectIdentity, Counter64, Integer32, Counter32, IpAddress, MibIdentifier, Gauge32, ModuleIdentity, Bits, iso, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "TimeTicks", "ObjectIdentity", "Counter64", "Integer32", "Counter32", "IpAddress", "MibIdentifier", "Gauge32", "ModuleIdentity", "Bits", "iso", "NotificationType")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
prvtTeParamMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 9))
prvtTeParamMIB.setRevisions(('2010-04-28 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: prvtTeParamMIB.setRevisionsDescriptions(('initial version',))
if mibBuilder.loadTexts: prvtTeParamMIB.setLastUpdated('201004280000Z')
if mibBuilder.loadTexts: prvtTeParamMIB.setOrganization('BATM Advanced Communication')
if mibBuilder.loadTexts: prvtTeParamMIB.setContactInfo('BATM/Telco Systems Support team\n         Email:\n         For North America: techsupport@telco.com\n         For North Europe: support@batm.de, info@batm.de\n         For the rest of the world: techsupport@telco.com')
if mibBuilder.loadTexts: prvtTeParamMIB.setDescription('The MIB module for management of TE-params entities.')
class PrvtTeLinkBandwidthSpeed(TextualConvention, Unsigned32):
    description = "Used in combination with PrvtTeLinkBandwidthUnits to specify a link's bandwidth."
    status = 'current'
    displayHint = 'd'

class PrvtTeLinkBandwidthUnits(TextualConvention, Integer32):
    description = "Used in combination with PrvtTeLinkBandwidthSpeed to specify a link's bandwidth."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("bps", 0), ("kbps", 1), ("mbps", 2), ("gbps", 3))

prvtTeParamMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 9, 1))
prvtTeParamLinkTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 9, 1, 2), )
if mibBuilder.loadTexts: prvtTeParamLinkTable.setStatus('current')
if mibBuilder.loadTexts: prvtTeParamLinkTable.setDescription('A table specifying the parameters of TE links.')
prvtTeParamLinkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 9, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: prvtTeParamLinkEntry.setStatus('current')
if mibBuilder.loadTexts: prvtTeParamLinkEntry.setDescription('An entry in prvtTeParamLinkTable.')
prvtTeParamLinkRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 9, 1, 2, 1, 1), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtTeParamLinkRowStatus.setStatus('current')
if mibBuilder.loadTexts: prvtTeParamLinkRowStatus.setDescription('The RowStatus entry for theprvtTeParamLinkTable.')
prvtTeParamLinkMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 9, 1, 2, 1, 2), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtTeParamLinkMetric.setReference('Link Bundling in MPLS Traffic Engineering (TE), RFC 4201')
if mibBuilder.loadTexts: prvtTeParamLinkMetric.setStatus('current')
if mibBuilder.loadTexts: prvtTeParamLinkMetric.setDescription('Traffic engineering metric (TEM) for the TE link.\n         The TEM is derived from its component links.\n         All component links within the TE link must have the same TEM.')
prvtTeParamLinkPhyBandwidthSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 9, 1, 2, 1, 3), PrvtTeLinkBandwidthSpeed()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtTeParamLinkPhyBandwidthSpeed.setStatus('current')
if mibBuilder.loadTexts: prvtTeParamLinkPhyBandwidthSpeed.setDescription('Used together with the prvtTeParamLinkPhyBandwidthUnits\n         object to specify the physical bandwidth for the TE link.')
prvtTeParamLinkPhyBandwidthUnits = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 9, 1, 2, 1, 4), PrvtTeLinkBandwidthUnits()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtTeParamLinkPhyBandwidthUnits.setStatus('current')
if mibBuilder.loadTexts: prvtTeParamLinkPhyBandwidthUnits.setDescription('Used together with the prvtTeParamLinkPhyBandwidthSpeed\n         object to specify the physical bandwidth for the TE link.')
prvtTeParamLinkMaxRsvBwSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 9, 1, 2, 1, 5), PrvtTeLinkBandwidthSpeed()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtTeParamLinkMaxRsvBwSpeed.setStatus('current')
if mibBuilder.loadTexts: prvtTeParamLinkMaxRsvBwSpeed.setDescription('Used together with the prvtTeParamLinkMaxRsvBwUnits\n         object to specify the maximum bandwidth for the TE link.')
prvtTeParamLinkMaxRsvBwUnits = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 9, 1, 2, 1, 6), PrvtTeLinkBandwidthUnits()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtTeParamLinkMaxRsvBwUnits.setStatus('current')
if mibBuilder.loadTexts: prvtTeParamLinkMaxRsvBwUnits.setDescription('Used together with the prvtTeParamLinkMaxRsvBwSpeed\n         object to specify the maximum bandwidth that can be reserved for the TE link.')
prvtTeParamLinkAdminGrpTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 9, 1, 3), )
if mibBuilder.loadTexts: prvtTeParamLinkAdminGrpTable.setStatus('current')
if mibBuilder.loadTexts: prvtTeParamLinkAdminGrpTable.setDescription('Table specifying the administrative groups to which a TE link belongs.')
prvtTeParamLinkAdminGrpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 9, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "PRVT-TE-PARAM-MIB", "prvtTeParamLinkAdminGrpId"))
if mibBuilder.loadTexts: prvtTeParamLinkAdminGrpEntry.setStatus('current')
if mibBuilder.loadTexts: prvtTeParamLinkAdminGrpEntry.setDescription('An entry in prvtTeParamLinkAdminGrpTable.')
prvtTeParamLinkAdminGrpId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 9, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32)))
if mibBuilder.loadTexts: prvtTeParamLinkAdminGrpId.setStatus('current')
if mibBuilder.loadTexts: prvtTeParamLinkAdminGrpId.setDescription('ID of the administrative group to which the TE link belongs.')
prvtTeParamLinkAdminGrpRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 9, 1, 3, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtTeParamLinkAdminGrpRowStatus.setStatus('current')
if mibBuilder.loadTexts: prvtTeParamLinkAdminGrpRowStatus.setDescription('The RowStatus entry for the prvtTeParamLinkAdminGrpTable.')
prvtTeParamAdminGroupTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 9, 1, 5), )
if mibBuilder.loadTexts: prvtTeParamAdminGroupTable.setStatus('current')
if mibBuilder.loadTexts: prvtTeParamAdminGroupTable.setDescription('Table storing the identifiers for an administrative group.')
prvtTeParamAdminGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 9, 1, 5, 1), ).setIndexNames((0, "PRVT-TE-PARAM-MIB", "prvtTeParamAdminGroupId"))
if mibBuilder.loadTexts: prvtTeParamAdminGroupEntry.setStatus('current')
if mibBuilder.loadTexts: prvtTeParamAdminGroupEntry.setDescription('prvtTeParamAdminGroupTable allows the specifying of a group-name to\n         each administrative group. Each group is uniquely identified by its\n         prvtTeParamAdminGroupId.')
prvtTeParamAdminGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 9, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32)))
if mibBuilder.loadTexts: prvtTeParamAdminGroupId.setStatus('current')
if mibBuilder.loadTexts: prvtTeParamAdminGroupId.setDescription('ID uniquely identifying an administrative group.')
prvtTeParamAdminGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 9, 1, 5, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtTeParamAdminGroupRowStatus.setStatus('current')
if mibBuilder.loadTexts: prvtTeParamAdminGroupRowStatus.setDescription('The RowStatus entry for theprvtTeParamAdminGroupTable.')
prvtTeParamAdminGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 9, 1, 5, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 15))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtTeParamAdminGroupName.setStatus('current')
if mibBuilder.loadTexts: prvtTeParamAdminGroupName.setDescription('The name of the administrative group.')
mibBuilder.exportSymbols("PRVT-TE-PARAM-MIB", prvtTeParamLinkMaxRsvBwSpeed=prvtTeParamLinkMaxRsvBwSpeed, prvtTeParamLinkAdminGrpRowStatus=prvtTeParamLinkAdminGrpRowStatus, prvtTeParamLinkPhyBandwidthUnits=prvtTeParamLinkPhyBandwidthUnits, prvtTeParamAdminGroupRowStatus=prvtTeParamAdminGroupRowStatus, prvtTeParamAdminGroupTable=prvtTeParamAdminGroupTable, prvtTeParamLinkMetric=prvtTeParamLinkMetric, prvtTeParamAdminGroupId=prvtTeParamAdminGroupId, prvtTeParamLinkAdminGrpEntry=prvtTeParamLinkAdminGrpEntry, prvtTeParamAdminGroupName=prvtTeParamAdminGroupName, prvtTeParamLinkRowStatus=prvtTeParamLinkRowStatus, prvtTeParamLinkEntry=prvtTeParamLinkEntry, PrvtTeLinkBandwidthSpeed=PrvtTeLinkBandwidthSpeed, prvtTeParamMIB=prvtTeParamMIB, prvtTeParamLinkPhyBandwidthSpeed=prvtTeParamLinkPhyBandwidthSpeed, prvtTeParamAdminGroupEntry=prvtTeParamAdminGroupEntry, PrvtTeLinkBandwidthUnits=PrvtTeLinkBandwidthUnits, PYSNMP_MODULE_ID=prvtTeParamMIB, prvtTeParamMIBObjects=prvtTeParamMIBObjects, prvtTeParamLinkAdminGrpTable=prvtTeParamLinkAdminGrpTable, prvtTeParamLinkMaxRsvBwUnits=prvtTeParamLinkMaxRsvBwUnits, prvtTeParamLinkTable=prvtTeParamLinkTable, prvtTeParamLinkAdminGrpId=prvtTeParamLinkAdminGrpId)
