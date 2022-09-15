#
# PySNMP MIB module CTRON-SSR-SERVICE-STATUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-SSR-SERVICE-STATUS-MIB
# Produced by pysmi-1.1.8 at Thu Sep 15 10:03:23 2022
# On host fv-az196-500 platform Linux version 5.15.0-1019-azure by user runner
# Using Python version 3.10.6 (main, Aug  3 2022, 07:09:11) [GCC 9.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ssrMibs, = mibBuilder.importSymbols("CTRON-SSR-SMI-MIB", "ssrMibs")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter32, NotificationType, iso, Integer32, Bits, Gauge32, IpAddress, MibIdentifier, TimeTicks, Counter64, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "NotificationType", "iso", "Integer32", "Bits", "Gauge32", "IpAddress", "MibIdentifier", "TimeTicks", "Counter64", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("CTRON-SSR-SERVICE-STATUS-MIB", serviceStatusRip=serviceStatusRip, serviceStatusRmon=serviceStatusRmon, ssCompliances=ssCompliances, serviceStatusLfap=serviceStatusLfap, ssConfGroupV11=ssConfGroupV11, ServiceStatus=ServiceStatus, ssGroups=ssGroups, serviceStatusIpxRip=serviceStatusIpxRip, serviceStatusStp=serviceStatusStp, serviceStatusPim=serviceStatusPim, ssConformance=ssConformance, serviceStatusIgmp=serviceStatusIgmp, ssConfGroupV10=ssConfGroupV10, PYSNMP_MODULE_ID=serviceStatusMIB, serviceStatusIpxSap=serviceStatusIpxSap, serviceStatusMIB=serviceStatusMIB, ssComplianceV10=ssComplianceV10, serviceStatusGroup=serviceStatusGroup, serviceStatusBgp=serviceStatusBgp, ssComplianceV11=ssComplianceV11, serviceStatusDvmrp=serviceStatusDvmrp, serviceStatusOspf=serviceStatusOspf)
