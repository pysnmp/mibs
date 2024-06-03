#
# PySNMP MIB module RBN-CPU-METER-CAP (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ericsson/RBN-CPU-METER-CAP
# Produced by pysmi-1.1.12 at Mon Jun  3 13:42:52 2024
# On host fv-az1530-906 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
rbnCapabilities, = mibBuilder.importSymbols("RBN-SMI", "rbnCapabilities")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Gauge32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, TimeTicks, IpAddress, ModuleIdentity, iso, MibIdentifier, NotificationType, Counter64, Unsigned32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "TimeTicks", "IpAddress", "ModuleIdentity", "iso", "MibIdentifier", "NotificationType", "Counter64", "Unsigned32", "Integer32", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rbnCpuMeterCap = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 4, 22))
rbnCpuMeterCap.setRevisions(('2011-12-13 18:00', '2011-06-15 00:00', '2010-11-01 00:00', '2003-10-14 00:00', '2003-07-07 00:00', '2003-02-11 00:00', '2002-06-26 00:00', '1999-06-16 23:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rbnCpuMeterCap.setRevisionsDescriptions(('Added rbnCpuMeterCap6.', 'Update DESCRIPTION clause of MODULE-IDENTITY\n                and PRODUCT-RELEASE clause of AGENT-CAPABILITIES.', 'Modified PRODUCT-RELEASE clause for consistent naming.\n                Updated CONTACT-INFO.', 'Added new OID: rbnCpuMeterCap5.', 'Added new OID: rbnCpuMeterCap4.', 'Added new OID: rbnCpuMeterCap3.', 'Updated CONTACT-INFO.  Added new OID: rbnCpuMeterCap2.', 'Initial version.',))
if mibBuilder.loadTexts: rbnCpuMeterCap.setLastUpdated('201112131800Z')
if mibBuilder.loadTexts: rbnCpuMeterCap.setOrganization('Ericsson Inc.')
if mibBuilder.loadTexts: rbnCpuMeterCap.setContactInfo('       Ericsson, Inc.\n\n                Postal: 100 Headquarters Dr.\n                        San Jose, CA  95134\n                        USA\n\n                 Phone: +1 408 750 5000\n                   Fax: +1 408 750 5599\n                ')
if mibBuilder.loadTexts: rbnCpuMeterCap.setDescription('The Agent Capabilities of the \n                CPU METER MIB (RBN-CPU-METER-MIB).\n\n                If this MIB implementation is platform-dependent,\n                the PRODUCT-RELEASE clause contains Ericsson SEOS version and\n                at least one of the following Ericsson product families:\n                    [SE]  SmartEdge Multi-service Edge Router (MSER) family\n                    [SM]  SM family of Metro Ethernet Service Transport platforms\n                    [SSR] Smart Service Router (SSR) family')
rbnCpuMeterCap1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 2352, 4, 22, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCpuMeterCap1 = rbnCpuMeterCap1.setProductRelease('AOS 3.0.X.X')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCpuMeterCap1 = rbnCpuMeterCap1.setStatus('current')
if mibBuilder.loadTexts: rbnCpuMeterCap1.setDescription('RBN-CPU-METER-MIB capabilities')
rbnCpuMeterCap2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 2352, 4, 22, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCpuMeterCap2 = rbnCpuMeterCap2.setProductRelease('SEOS 2.3.3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCpuMeterCap2 = rbnCpuMeterCap2.setStatus('current')
if mibBuilder.loadTexts: rbnCpuMeterCap2.setDescription('RBN-CPU-METER-MIB capabilities')
rbnCpuMeterCap3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 2352, 4, 22, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCpuMeterCap3 = rbnCpuMeterCap3.setProductRelease('AOS 6.0.X.X')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCpuMeterCap3 = rbnCpuMeterCap3.setStatus('current')
if mibBuilder.loadTexts: rbnCpuMeterCap3.setDescription('RBN-CPU-METER-MIB capabilities')
rbnCpuMeterCap4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 2352, 4, 22, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCpuMeterCap4 = rbnCpuMeterCap4.setProductRelease('SEOS 2.5.4')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCpuMeterCap4 = rbnCpuMeterCap4.setStatus('current')
if mibBuilder.loadTexts: rbnCpuMeterCap4.setDescription('RBN-CPU-METER-MIB capabilities')
rbnCpuMeterCap5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 2352, 4, 22, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCpuMeterCap5 = rbnCpuMeterCap5.setProductRelease('SEOS 2.6.3 [SE]; SEOS 6.3.X [SM]; SEOS 11.1.X [SSR]')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCpuMeterCap5 = rbnCpuMeterCap5.setStatus('current')
if mibBuilder.loadTexts: rbnCpuMeterCap5.setDescription('RBN-CPU-METER-MIB capabilities')
rbnCpuMeterCap6 = AgentCapabilities((1, 3, 6, 1, 4, 1, 2352, 4, 22, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCpuMeterCap6 = rbnCpuMeterCap6.setProductRelease('IPOS 11.2.X')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCpuMeterCap6 = rbnCpuMeterCap6.setStatus('current')
if mibBuilder.loadTexts: rbnCpuMeterCap6.setDescription('RBN-CPU-METER-MIB capabilities')
mibBuilder.exportSymbols("RBN-CPU-METER-CAP", rbnCpuMeterCap1=rbnCpuMeterCap1, PYSNMP_MODULE_ID=rbnCpuMeterCap, rbnCpuMeterCap6=rbnCpuMeterCap6, rbnCpuMeterCap4=rbnCpuMeterCap4, rbnCpuMeterCap3=rbnCpuMeterCap3, rbnCpuMeterCap=rbnCpuMeterCap, rbnCpuMeterCap2=rbnCpuMeterCap2, rbnCpuMeterCap5=rbnCpuMeterCap5)
