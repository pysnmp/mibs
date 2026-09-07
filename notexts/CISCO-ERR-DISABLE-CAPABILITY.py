#
# PySNMP MIB module CISCO-ERR-DISABLE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ERR-DISABLE-CAPABILITY
# Source digest sha256:d7d7e20b56a24f43a5af144cfedc93726d9281ae1f76086ac05af319e431821f
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
TimeIntervalSec, = mibBuilder.importSymbols("CISCO-TC", "TimeIntervalSec")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoErrDisableCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 589))
ciscoErrDisableCapability.setRevisions(('2013-09-25 00:00', '2010-10-29 00:00', '2010-05-05 00:00', '2010-03-11 00:00',))
if mibBuilder.loadTexts: ciscoErrDisableCapability.setLastUpdated('2013-09-25 00:00')
if mibBuilder.loadTexts: ciscoErrDisableCapability.setOrganization('Cisco Systems, Inc.')
cErrDisableCapV12R0233SXI4PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 589, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cErrDisableCapV12R0233SXI4PCat6K = cErrDisableCapV12R0233SXI4PCat6K.setProductRelease('Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cErrDisableCapV12R0233SXI4PCat6K = cErrDisableCapV12R0233SXI4PCat6K.setStatus('current')
cErrDisableCapV12R0254SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 589, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cErrDisableCapV12R0254SGPCat4K = cErrDisableCapV12R0254SGPCat4K.setProductRelease('Cisco IOS 12.2(54)SG on CAT4K family switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cErrDisableCapV12R0254SGPCat4K = cErrDisableCapV12R0254SGPCat4K.setStatus('current')
cErrDisableCapV12R0250SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 589, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cErrDisableCapV12R0250SYPCat6K = cErrDisableCapV12R0250SYPCat6K.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cErrDisableCapV12R0250SYPCat6K = cErrDisableCapV12R0250SYPCat6K.setStatus('current')
cErrDisableCapV15R0102SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 589, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cErrDisableCapV15R0102SYPCat6K = cErrDisableCapV15R0102SYPCat6K.setProductRelease('Cisco IOS 15.1(2)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cErrDisableCapV15R0102SYPCat6K = cErrDisableCapV15R0102SYPCat6K.setStatus('current')
mibBuilder.exportSymbols("CISCO-ERR-DISABLE-CAPABILITY", PYSNMP_MODULE_ID=ciscoErrDisableCapability, cErrDisableCapV12R0233SXI4PCat6K=cErrDisableCapV12R0233SXI4PCat6K, cErrDisableCapV12R0250SYPCat6K=cErrDisableCapV12R0250SYPCat6K, cErrDisableCapV12R0254SGPCat4K=cErrDisableCapV12R0254SGPCat4K, cErrDisableCapV15R0102SYPCat6K=cErrDisableCapV15R0102SYPCat6K, ciscoErrDisableCapability=ciscoErrDisableCapability)
