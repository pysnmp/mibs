#
# PySNMP MIB module CTRON-SSR-SERVICE-STATUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-SSR-SERVICE-STATUS-MIB
# Produced by pysmi-1.1.8 at Thu Sep  7 14:14:57 2023
# On host fv-az548-537 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
ssrMibs, = mibBuilder.importSymbols("CTRON-SSR-SMI-MIB", "ssrMibs")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
IpAddress, iso, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter32, Integer32, Unsigned32, Counter64, Bits, ModuleIdentity, ObjectIdentity, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "iso", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter32", "Integer32", "Unsigned32", "Counter64", "Bits", "ModuleIdentity", "ObjectIdentity", "TimeTicks", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
serviceStatusMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 2501, 1, 700))
serviceStatusMIB.setRevisions(('2000-07-15 00:00', '1998-08-04 00:00', '1998-04-08 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: serviceStatusMIB.setRevisionsDescriptions(('Revision 2.0 Update contact information for Enterasys Networks as this mib\n          is found on the Riverstione RS product line as well as Enterasys SSR product line.', 'Revision 1.1 Flow Accounting Function and RMON visible.', 'Revision 1.0 Initial mib revision.',))
if mibBuilder.loadTexts: serviceStatusMIB.setLastUpdated('200007150000Z')
if mibBuilder.loadTexts: serviceStatusMIB.setOrganization('Cabletron Systems, Inc.')
if mibBuilder.loadTexts: serviceStatusMIB.setContactInfo('Enterasys Networks\n     35 Industrial Way, P.O. Box 5005\n     Rochester, NH 03867-0505\n     (603) 332-9400\n     support@enterasys.com\n     http://www.enterasys.com')
if mibBuilder.loadTexts: serviceStatusMIB.setDescription('This module describes a schema for accessing the\n      Smart Switch Router subsystems.')
serviceStatusGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 1, 4))
class ServiceStatus(TextualConvention, Integer32):
    description = 'The current state of the service: started indicates \n        the service is configured and running. Stopped indicates\n        the service is administratively down. notWorking indicates\n        the service has failed.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("started", 1), ("stopped", 2), ("notWorking", 3))

serviceStatusRip = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 4, 1), ServiceStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serviceStatusRip.setStatus('current')
if mibBuilder.loadTexts: serviceStatusRip.setDescription('The current status of RIP in the switch.')
serviceStatusOspf = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 4, 2), ServiceStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serviceStatusOspf.setStatus('current')
if mibBuilder.loadTexts: serviceStatusOspf.setDescription('The current status of OSPF in the switch.')
serviceStatusBgp = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 4, 3), ServiceStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serviceStatusBgp.setStatus('current')
if mibBuilder.loadTexts: serviceStatusBgp.setDescription('The current status of BGP in the switch.')
serviceStatusDvmrp = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 4, 4), ServiceStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serviceStatusDvmrp.setStatus('current')
if mibBuilder.loadTexts: serviceStatusDvmrp.setDescription('The current status of DVMRP in the switch.')
serviceStatusIgmp = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 4, 5), ServiceStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serviceStatusIgmp.setStatus('current')
if mibBuilder.loadTexts: serviceStatusIgmp.setDescription('The current status of IGMP in the switch.')
serviceStatusPim = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 4, 6), ServiceStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serviceStatusPim.setStatus('current')
if mibBuilder.loadTexts: serviceStatusPim.setDescription('The current status of PIM in the switch.')
serviceStatusStp = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 4, 7), ServiceStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serviceStatusStp.setStatus('current')
if mibBuilder.loadTexts: serviceStatusStp.setDescription('The current status of STP in the switch.')
serviceStatusIpxRip = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 4, 8), ServiceStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serviceStatusIpxRip.setStatus('current')
if mibBuilder.loadTexts: serviceStatusIpxRip.setDescription('The current status of IPX in the switch.')
serviceStatusIpxSap = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 4, 9), ServiceStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serviceStatusIpxSap.setStatus('current')
if mibBuilder.loadTexts: serviceStatusIpxSap.setDescription('The current status of IPX in the switch.')
serviceStatusLfap = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 4, 10), ServiceStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serviceStatusLfap.setStatus('current')
if mibBuilder.loadTexts: serviceStatusLfap.setDescription('The current status of Lightweight Flow Accounting Protocol.')
serviceStatusRmon = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 4, 11), ServiceStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serviceStatusRmon.setStatus('current')
if mibBuilder.loadTexts: serviceStatusRmon.setDescription('The current status of RMON.')
ssConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 1, 700, 2))
ssCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 1, 700, 2, 1))
ssGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 1, 700, 2, 2))
ssComplianceV10 = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 2501, 1, 700, 2, 2, 1, 1)).setObjects()

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ssComplianceV10 = ssComplianceV10.setStatus('obsolete')
if mibBuilder.loadTexts: ssComplianceV10.setDescription('The compliance statement for the CTRON-SSR-SERVICE-STATUS-MIB.')
ssComplianceV11 = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 2501, 1, 700, 2, 2, 1, 2)).setObjects(("CTRON-SSR-SERVICE-STATUS-MIB", "ssConfGroupV11"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ssComplianceV11 = ssComplianceV11.setStatus('current')
if mibBuilder.loadTexts: ssComplianceV11.setDescription('The compliance statement for the CTRON-SSR-SERVICE-STATUS-MIB.')
ssConfGroupV10 = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 2501, 1, 700, 2, 2, 1)).setObjects(("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusRip"), ("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusOspf"), ("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusBgp"), ("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusDvmrp"), ("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusIgmp"), ("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusPim"), ("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusStp"), ("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusIpxRip"), ("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusIpxSap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ssConfGroupV10 = ssConfGroupV10.setStatus('obsolete')
if mibBuilder.loadTexts: ssConfGroupV10.setDescription('A set of managed objects that make up version 1.0 of the SSR Service Status mib.')
ssConfGroupV11 = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 2501, 1, 700, 2, 2, 2)).setObjects(("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusRip"), ("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusOspf"), ("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusBgp"), ("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusDvmrp"), ("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusIgmp"), ("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusPim"), ("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusStp"), ("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusIpxRip"), ("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusIpxSap"), ("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusLfap"), ("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusRmon"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ssConfGroupV11 = ssConfGroupV11.setStatus('current')
if mibBuilder.loadTexts: ssConfGroupV11.setDescription('A set of managed objects that make up version 1.1 of the SSR Service Status mib.')
mibBuilder.exportSymbols("CTRON-SSR-SERVICE-STATUS-MIB", serviceStatusRip=serviceStatusRip, serviceStatusRmon=serviceStatusRmon, serviceStatusLfap=serviceStatusLfap, ssConfGroupV10=ssConfGroupV10, serviceStatusPim=serviceStatusPim, ssGroups=ssGroups, serviceStatusIpxSap=serviceStatusIpxSap, ssComplianceV10=ssComplianceV10, PYSNMP_MODULE_ID=serviceStatusMIB, serviceStatusIpxRip=serviceStatusIpxRip, serviceStatusDvmrp=serviceStatusDvmrp, serviceStatusGroup=serviceStatusGroup, serviceStatusBgp=serviceStatusBgp, ssConformance=ssConformance, serviceStatusOspf=serviceStatusOspf, serviceStatusStp=serviceStatusStp, ssCompliances=ssCompliances, serviceStatusIgmp=serviceStatusIgmp, ssComplianceV11=ssComplianceV11, ServiceStatus=ServiceStatus, serviceStatusMIB=serviceStatusMIB, ssConfGroupV11=ssConfGroupV11)
