#
# PySNMP MIB module RBN-CPU-METER-CAP (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ericsson/RBN-CPU-METER-CAP
# Produced by pysmi-1.1.12 at Tue May 28 12:11:51 2024
# On host fv-az1567-4 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
rbnCapabilities, = mibBuilder.importSymbols("RBN-SMI", "rbnCapabilities")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
TimeTicks, ModuleIdentity, iso, ObjectIdentity, Unsigned32, Counter64, Bits, Counter32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, NotificationType, Integer32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ModuleIdentity", "iso", "ObjectIdentity", "Unsigned32", "Counter64", "Bits", "Counter32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "NotificationType", "Integer32", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rbnCpuMeterCap = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 4, 22))
rbnCpuMeterCap.setRevisions(('2011-12-13 18:00', '2011-06-15 00:00', '2010-11-01 00:00', '2003-10-14 00:00', '2003-07-07 00:00', '2003-02-11 00:00', '2002-06-26 00:00', '1999-06-16 23:00',))
if mibBuilder.loadTexts: rbnCpuMeterCap.setLastUpdated('201112131800Z')
if mibBuilder.loadTexts: rbnCpuMeterCap.setOrganization('Ericsson Inc.')
rbnCpuMeterCap1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 2352, 4, 22, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCpuMeterCap1 = rbnCpuMeterCap1.setProductRelease('AOS 3.0.X.X')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCpuMeterCap1 = rbnCpuMeterCap1.setStatus('current')
rbnCpuMeterCap2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 2352, 4, 22, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCpuMeterCap2 = rbnCpuMeterCap2.setProductRelease('SEOS 2.3.3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCpuMeterCap2 = rbnCpuMeterCap2.setStatus('current')
rbnCpuMeterCap3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 2352, 4, 22, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCpuMeterCap3 = rbnCpuMeterCap3.setProductRelease('AOS 6.0.X.X')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCpuMeterCap3 = rbnCpuMeterCap3.setStatus('current')
rbnCpuMeterCap4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 2352, 4, 22, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCpuMeterCap4 = rbnCpuMeterCap4.setProductRelease('SEOS 2.5.4')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCpuMeterCap4 = rbnCpuMeterCap4.setStatus('current')
rbnCpuMeterCap5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 2352, 4, 22, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCpuMeterCap5 = rbnCpuMeterCap5.setProductRelease('SEOS 2.6.3 [SE]; SEOS 6.3.X [SM]; SEOS 11.1.X [SSR]')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCpuMeterCap5 = rbnCpuMeterCap5.setStatus('current')
rbnCpuMeterCap6 = AgentCapabilities((1, 3, 6, 1, 4, 1, 2352, 4, 22, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCpuMeterCap6 = rbnCpuMeterCap6.setProductRelease('IPOS 11.2.X')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCpuMeterCap6 = rbnCpuMeterCap6.setStatus('current')
mibBuilder.exportSymbols("RBN-CPU-METER-CAP", PYSNMP_MODULE_ID=rbnCpuMeterCap, rbnCpuMeterCap4=rbnCpuMeterCap4, rbnCpuMeterCap2=rbnCpuMeterCap2, rbnCpuMeterCap6=rbnCpuMeterCap6, rbnCpuMeterCap1=rbnCpuMeterCap1, rbnCpuMeterCap=rbnCpuMeterCap, rbnCpuMeterCap5=rbnCpuMeterCap5, rbnCpuMeterCap3=rbnCpuMeterCap3)
