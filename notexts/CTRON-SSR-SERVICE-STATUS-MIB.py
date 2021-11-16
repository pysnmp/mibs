#
# PySNMP MIB module CTRON-SSR-SERVICE-STATUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-SSR-SERVICE-STATUS-MIB
# Produced by pysmi-1.1.0 at Tue Nov 16 12:09:08 2021
# On host fv-az121-894 platform Linux version 5.11.0-1020-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ssrMibs, = mibBuilder.importSymbols("CTRON-SSR-SMI-MIB", "ssrMibs")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter32, Counter64, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Unsigned32, Bits, NotificationType, TimeTicks, ObjectIdentity, Gauge32, Integer32, ModuleIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Unsigned32", "Bits", "NotificationType", "TimeTicks", "ObjectIdentity", "Gauge32", "Integer32", "ModuleIdentity", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
serviceStatusMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 2501, 1, 700))
serviceStatusMIB.setRevisions(('2000-07-15 00:00', '1998-08-04 00:00', '1998-04-08 12:00',))
if mibBuilder.loadTexts: serviceStatusMIB.setLastUpdated('200007150000Z')
if mibBuilder.loadTexts: serviceStatusMIB.setOrganization('Cabletron Systems, Inc.')
serviceStatusGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 1, 4))
class ServiceStatus(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("started", 1), ("stopped", 2), ("notWorking", 3))

serviceStatusRip = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 4, 1), ServiceStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serviceStatusRip.setStatus('current')
serviceStatusOspf = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 4, 2), ServiceStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serviceStatusOspf.setStatus('current')
serviceStatusBgp = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 4, 3), ServiceStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serviceStatusBgp.setStatus('current')
serviceStatusDvmrp = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 4, 4), ServiceStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serviceStatusDvmrp.setStatus('current')
serviceStatusIgmp = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 4, 5), ServiceStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serviceStatusIgmp.setStatus('current')
serviceStatusPim = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 4, 6), ServiceStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serviceStatusPim.setStatus('current')
serviceStatusStp = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 4, 7), ServiceStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serviceStatusStp.setStatus('current')
serviceStatusIpxRip = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 4, 8), ServiceStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serviceStatusIpxRip.setStatus('current')
serviceStatusIpxSap = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 4, 9), ServiceStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serviceStatusIpxSap.setStatus('current')
serviceStatusLfap = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 4, 10), ServiceStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serviceStatusLfap.setStatus('current')
serviceStatusRmon = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 4, 11), ServiceStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serviceStatusRmon.setStatus('current')
ssConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 1, 700, 2))
ssCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 1, 700, 2, 1))
ssGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 1, 700, 2, 2))
ssComplianceV10 = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 2501, 1, 700, 2, 2, 1, 1)).setObjects()

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ssComplianceV10 = ssComplianceV10.setStatus('obsolete')
ssComplianceV11 = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 2501, 1, 700, 2, 2, 1, 2)).setObjects(("CTRON-SSR-SERVICE-STATUS-MIB", "ssConfGroupV11"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ssComplianceV11 = ssComplianceV11.setStatus('current')
ssConfGroupV10 = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 2501, 1, 700, 2, 2, 1)).setObjects(("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusRip"), ("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusOspf"), ("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusBgp"), ("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusDvmrp"), ("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusIgmp"), ("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusPim"), ("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusStp"), ("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusIpxRip"), ("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusIpxSap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ssConfGroupV10 = ssConfGroupV10.setStatus('obsolete')
ssConfGroupV11 = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 2501, 1, 700, 2, 2, 2)).setObjects(("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusRip"), ("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusOspf"), ("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusBgp"), ("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusDvmrp"), ("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusIgmp"), ("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusPim"), ("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusStp"), ("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusIpxRip"), ("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusIpxSap"), ("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusLfap"), ("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusRmon"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ssConfGroupV11 = ssConfGroupV11.setStatus('current')
mibBuilder.exportSymbols("CTRON-SSR-SERVICE-STATUS-MIB", serviceStatusPim=serviceStatusPim, serviceStatusIpxRip=serviceStatusIpxRip, ssCompliances=ssCompliances, ssConfGroupV10=ssConfGroupV10, PYSNMP_MODULE_ID=serviceStatusMIB, serviceStatusLfap=serviceStatusLfap, ssConfGroupV11=ssConfGroupV11, ssConformance=ssConformance, serviceStatusMIB=serviceStatusMIB, serviceStatusIpxSap=serviceStatusIpxSap, serviceStatusGroup=serviceStatusGroup, ssComplianceV11=ssComplianceV11, serviceStatusRmon=serviceStatusRmon, serviceStatusIgmp=serviceStatusIgmp, serviceStatusDvmrp=serviceStatusDvmrp, ssComplianceV10=ssComplianceV10, serviceStatusStp=serviceStatusStp, serviceStatusOspf=serviceStatusOspf, ServiceStatus=ServiceStatus, serviceStatusRip=serviceStatusRip, ssGroups=ssGroups, serviceStatusBgp=serviceStatusBgp)
