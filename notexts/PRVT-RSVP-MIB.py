#
# PySNMP MIB module PRVT-RSVP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binox/PRVT-RSVP-MIB
# Produced by pysmi-1.1.3 at Tue Dec  7 14:17:50 2021
# On host fv-az33-388 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
mpls, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "mpls")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, NotificationType, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Unsigned32, Counter32, Counter64, ModuleIdentity, Bits, ObjectIdentity, iso, Integer32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "NotificationType", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Unsigned32", "Counter32", "Counter64", "ModuleIdentity", "Bits", "ObjectIdentity", "iso", "Integer32", "Gauge32")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
prvtRsvpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 7))
prvtRsvpMIB.setRevisions(('2011-03-21 00:00', '2009-02-10 00:00',))
if mibBuilder.loadTexts: prvtRsvpMIB.setLastUpdated('201103210000Z')
if mibBuilder.loadTexts: prvtRsvpMIB.setOrganization('BATM Advanced Communication')
class PrvtRsvpAdminStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class PrvtRsvpOperStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("up", 1), ("down", 2), ("goingUp", 3), ("goingDown", 4), ("actFailed", 5))

class PrvtRsvpIndex(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'

prvtRsvpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 7, 1))
prvtRsvpProductTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 7, 1, 1), )
if mibBuilder.loadTexts: prvtRsvpProductTable.setStatus('current')
prvtRsvpProductEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 7, 1, 1, 1), ).setIndexNames((0, "PRVT-RSVP-MIB", "prvtRsvpProductIndex"))
if mibBuilder.loadTexts: prvtRsvpProductEntry.setStatus('current')
prvtRsvpProductIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 7, 1, 1, 1, 1), PrvtRsvpIndex())
if mibBuilder.loadTexts: prvtRsvpProductIndex.setStatus('current')
prvtRsvpProductRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 7, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRsvpProductRowStatus.setStatus('current')
prvtRsvpProductAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 7, 1, 1, 1, 3), PrvtRsvpAdminStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRsvpProductAdminStatus.setStatus('current')
prvtRsvpProductOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 7, 1, 1, 1, 4), PrvtRsvpOperStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRsvpProductOperStatus.setStatus('current')
prvtRsvpProductProtocolExtensions = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 7, 1, 1, 1, 5), Bits().clone(namedValues=NamedValues(("bypassFastReroute", 0), ("detourFastReroute", 1), ("noResAffOnInIf", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRsvpProductProtocolExtensions.setStatus('current')
prvtRsvpProductFastRerouteCaps = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 7, 1, 1, 1, 6), Bits().clone(namedValues=NamedValues(("fastReroutePLR", 0), ("fastRerouteMP", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRsvpProductFastRerouteCaps.setStatus('current')
mibBuilder.exportSymbols("PRVT-RSVP-MIB", PrvtRsvpAdminStatus=PrvtRsvpAdminStatus, PrvtRsvpIndex=PrvtRsvpIndex, prvtRsvpObjects=prvtRsvpObjects, prvtRsvpProductProtocolExtensions=prvtRsvpProductProtocolExtensions, prvtRsvpProductOperStatus=prvtRsvpProductOperStatus, prvtRsvpProductIndex=prvtRsvpProductIndex, PrvtRsvpOperStatus=PrvtRsvpOperStatus, prvtRsvpProductEntry=prvtRsvpProductEntry, prvtRsvpProductTable=prvtRsvpProductTable, prvtRsvpMIB=prvtRsvpMIB, PYSNMP_MODULE_ID=prvtRsvpMIB, prvtRsvpProductFastRerouteCaps=prvtRsvpProductFastRerouteCaps, prvtRsvpProductAdminStatus=prvtRsvpProductAdminStatus, prvtRsvpProductRowStatus=prvtRsvpProductRowStatus)
