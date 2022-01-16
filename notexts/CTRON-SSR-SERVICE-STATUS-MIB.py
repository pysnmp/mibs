#
# PySNMP MIB module CTRON-SSR-SERVICE-STATUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-SSR-SERVICE-STATUS-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:59:10 2022
# On host fv-az74-933 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
ssrMibs, = mibBuilder.importSymbols("CTRON-SSR-SMI-MIB", "ssrMibs")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter64, Integer32, Bits, ObjectIdentity, Unsigned32, Gauge32, IpAddress, iso, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter32, NotificationType, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Integer32", "Bits", "ObjectIdentity", "Unsigned32", "Gauge32", "IpAddress", "iso", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter32", "NotificationType", "MibIdentifier")
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
mibBuilder.exportSymbols("CTRON-SSR-SERVICE-STATUS-MIB", serviceStatusPim=serviceStatusPim, serviceStatusOspf=serviceStatusOspf, ssCompliances=ssCompliances, ssGroups=ssGroups, serviceStatusIpxRip=serviceStatusIpxRip, serviceStatusLfap=serviceStatusLfap, serviceStatusMIB=serviceStatusMIB, serviceStatusRmon=serviceStatusRmon, PYSNMP_MODULE_ID=serviceStatusMIB, serviceStatusGroup=serviceStatusGroup, ssComplianceV10=ssComplianceV10, serviceStatusStp=serviceStatusStp, ssConfGroupV10=ssConfGroupV10, ssConformance=ssConformance, serviceStatusRip=serviceStatusRip, serviceStatusIpxSap=serviceStatusIpxSap, serviceStatusIgmp=serviceStatusIgmp, serviceStatusBgp=serviceStatusBgp, ServiceStatus=ServiceStatus, ssComplianceV11=ssComplianceV11, serviceStatusDvmrp=serviceStatusDvmrp, ssConfGroupV11=ssConfGroupV11)
