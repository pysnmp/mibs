#
# PySNMP MIB module PRVT-CR-LDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binox/PRVT-CR-LDP-MIB
# Produced by pysmi-1.1.3 at Wed Dec  8 18:20:48 2021
# On host fv-az74-115 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
mpls, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "mpls")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, ModuleIdentity, Counter64, Gauge32, ObjectIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, MibIdentifier, TimeTicks, Integer32, Counter32, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "MibIdentifier", "TimeTicks", "Integer32", "Counter32", "Bits", "Unsigned32")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
prvtCrLdpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 3))
prvtCrLdpMIB.setRevisions(('2008-01-01 00:00',))
if mibBuilder.loadTexts: prvtCrLdpMIB.setLastUpdated('200801010000Z')
if mibBuilder.loadTexts: prvtCrLdpMIB.setOrganization('BATM Advanced Communication')
class PrvtCrldpIndex(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'

prvtCrLdpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 3, 1))
prvtcrldpSigTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 3, 1, 1), )
if mibBuilder.loadTexts: prvtcrldpSigTable.setStatus('current')
prvtcrldpSigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 3, 1, 1, 1), ).setIndexNames((0, "PRVT-CR-LDP-MIB", "prvtcrldpSigIndex"))
if mibBuilder.loadTexts: prvtcrldpSigEntry.setStatus('current')
prvtcrldpSigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 3, 1, 1, 1, 1), PrvtCrldpIndex())
if mibBuilder.loadTexts: prvtcrldpSigIndex.setStatus('current')
prvtcrldpSigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 3, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtcrldpSigRowStatus.setStatus('current')
prvtcrldpPmTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 3, 1, 2), )
if mibBuilder.loadTexts: prvtcrldpPmTable.setStatus('current')
prvtcrldpPmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 3, 1, 2, 1), ).setIndexNames((0, "PRVT-CR-LDP-MIB", "prvtcrldpPmIndex"))
if mibBuilder.loadTexts: prvtcrldpPmEntry.setStatus('current')
prvtcrldpPmIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 3, 1, 2, 1, 1), PrvtCrldpIndex())
if mibBuilder.loadTexts: prvtcrldpPmIndex.setStatus('current')
prvtcrldpPmRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 3, 1, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtcrldpPmRowStatus.setStatus('current')
mibBuilder.exportSymbols("PRVT-CR-LDP-MIB", prvtcrldpPmIndex=prvtcrldpPmIndex, prvtCrLdpObjects=prvtCrLdpObjects, prvtcrldpPmTable=prvtcrldpPmTable, PYSNMP_MODULE_ID=prvtCrLdpMIB, PrvtCrldpIndex=PrvtCrldpIndex, prvtcrldpPmRowStatus=prvtcrldpPmRowStatus, prvtcrldpPmEntry=prvtcrldpPmEntry, prvtcrldpSigEntry=prvtcrldpSigEntry, prvtcrldpSigTable=prvtcrldpSigTable, prvtCrLdpMIB=prvtCrLdpMIB, prvtcrldpSigRowStatus=prvtcrldpSigRowStatus, prvtcrldpSigIndex=prvtcrldpSigIndex)
