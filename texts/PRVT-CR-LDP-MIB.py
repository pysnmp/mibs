#
# PySNMP MIB module PRVT-CR-LDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binox/PRVT-CR-LDP-MIB
# Produced by pysmi-1.1.3 at Tue Dec  7 17:25:04 2021
# On host fv-az121-73 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
mpls, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "mpls")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, TimeTicks, ModuleIdentity, ObjectIdentity, NotificationType, Unsigned32, Counter32, IpAddress, Counter64, Bits, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "TimeTicks", "ModuleIdentity", "ObjectIdentity", "NotificationType", "Unsigned32", "Counter32", "IpAddress", "Counter64", "Bits", "MibIdentifier")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
prvtCrLdpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 3))
prvtCrLdpMIB.setRevisions(('2008-01-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: prvtCrLdpMIB.setRevisionsDescriptions(('Initial',))
if mibBuilder.loadTexts: prvtCrLdpMIB.setLastUpdated('200801010000Z')
if mibBuilder.loadTexts: prvtCrLdpMIB.setOrganization('BATM Advanced Communication')
if mibBuilder.loadTexts: prvtCrLdpMIB.setContactInfo('BATM/Telco Systems Support team\n         Email:\n         For North America: techsupport@telco.com\n         For North Europe: support@batm.de, info@batm.de\n         For the rest of the world: techsupport@telco.com')
if mibBuilder.loadTexts: prvtCrLdpMIB.setDescription('The MIB module for management of the PRVT-CR-LDP')
class PrvtCrldpIndex(TextualConvention, Unsigned32):
    description = 'A general purpose SNMP index into the prvtHafEntity table.'
    status = 'current'
    displayHint = 'd'

prvtCrLdpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 3, 1))
prvtcrldpSigTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 3, 1, 1), )
if mibBuilder.loadTexts: prvtcrldpSigTable.setStatus('current')
if mibBuilder.loadTexts: prvtcrldpSigTable.setDescription('The table of active instances of PRVT-CR-LDP Signaling.')
prvtcrldpSigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 3, 1, 1, 1), ).setIndexNames((0, "PRVT-CR-LDP-MIB", "prvtcrldpSigIndex"))
if mibBuilder.loadTexts: prvtcrldpSigEntry.setStatus('current')
if mibBuilder.loadTexts: prvtcrldpSigEntry.setDescription('Each of these entries represents an instance of\n         PRVT-CR-LDP Signaling running in the HAF. Some of these instances\n         will be the primary, and others may be backups.')
prvtcrldpSigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 3, 1, 1, 1, 1), PrvtCrldpIndex())
if mibBuilder.loadTexts: prvtcrldpSigIndex.setStatus('current')
if mibBuilder.loadTexts: prvtcrldpSigIndex.setDescription('The index of this prvtcrldpSigEntry. This is the\n         HAF entity index passed on the product create\n         parameters.')
prvtcrldpSigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 3, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtcrldpSigRowStatus.setStatus('current')
if mibBuilder.loadTexts: prvtcrldpSigRowStatus.setDescription("Used to create and delete a PRVT-CR-LDP Signaling Table entry.\n         When this object is set to 'active', only the\n         prvtcrldpSigAdminStatus object in the row may be modified.")
prvtcrldpPmTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 3, 1, 2), )
if mibBuilder.loadTexts: prvtcrldpPmTable.setStatus('current')
if mibBuilder.loadTexts: prvtcrldpPmTable.setDescription('The table of active instances of PRVT-CR-LDP Path Manager.')
prvtcrldpPmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 3, 1, 2, 1), ).setIndexNames((0, "PRVT-CR-LDP-MIB", "prvtcrldpPmIndex"))
if mibBuilder.loadTexts: prvtcrldpPmEntry.setStatus('current')
if mibBuilder.loadTexts: prvtcrldpPmEntry.setDescription('Each of these entries represents an instance of\n         PRVT-CR-LDP Path Manager running in the HAF. Some of these instances\n         will be the primary, and others may be backups.')
prvtcrldpPmIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 3, 1, 2, 1, 1), PrvtCrldpIndex())
if mibBuilder.loadTexts: prvtcrldpPmIndex.setStatus('current')
if mibBuilder.loadTexts: prvtcrldpPmIndex.setDescription('The index of this prvtcrldpPmEntry. This is the\n         HAF entity index passed on the product create\n         parameters.')
prvtcrldpPmRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 3, 1, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtcrldpPmRowStatus.setStatus('current')
if mibBuilder.loadTexts: prvtcrldpPmRowStatus.setDescription("Used to create and delete a PRVT-CR-LDP Path Manager Table entry.\n         When this object is set to 'active', only the\n         prvtcrldpPmAdminStatus object in the row may be modified.")
mibBuilder.exportSymbols("PRVT-CR-LDP-MIB", prvtcrldpPmTable=prvtcrldpPmTable, prvtcrldpSigEntry=prvtcrldpSigEntry, prvtcrldpSigTable=prvtcrldpSigTable, prvtCrLdpObjects=prvtCrLdpObjects, prvtcrldpSigIndex=prvtcrldpSigIndex, PrvtCrldpIndex=PrvtCrldpIndex, prvtCrLdpMIB=prvtCrLdpMIB, prvtcrldpPmIndex=prvtcrldpPmIndex, prvtcrldpPmEntry=prvtcrldpPmEntry, PYSNMP_MODULE_ID=prvtCrLdpMIB, prvtcrldpSigRowStatus=prvtcrldpSigRowStatus, prvtcrldpPmRowStatus=prvtcrldpPmRowStatus)
