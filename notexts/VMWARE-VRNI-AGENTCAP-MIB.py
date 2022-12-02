#
# PySNMP MIB module VMWARE-VRNI-AGENTCAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/vmware/VMWARE-VRNI-AGENTCAP-MIB
# Produced by pysmi-1.1.8 at Fri Dec  2 17:16:15 2022
# On host fv-az563-842 platform Linux version 5.15.0-1023-azure by user runner
# Using Python version 3.10.8 (main, Oct 18 2022, 06:44:51) [GCC 11.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
iso, Gauge32, Bits, ObjectIdentity, Integer32, TimeTicks, MibIdentifier, Unsigned32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ModuleIdentity, Counter32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Gauge32", "Bits", "ObjectIdentity", "Integer32", "TimeTicks", "MibIdentifier", "Unsigned32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ModuleIdentity", "Counter32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
vmwareAgentCapabilities, = mibBuilder.importSymbols("VMWARE-ROOT-MIB", "vmwareAgentCapabilities")
vmwVRNIAgentCapabilityMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6876, 70, 125))
vmwVRNIAgentCapabilityMIB.setRevisions(('2020-05-20 00:00', '2019-08-19 00:00', '2019-06-06 00:00', '2019-03-22 00:00', '2018-12-04 00:00', '2018-09-12 00:00', '2017-10-13 00:00', '2017-09-05 00:00', '2017-06-01 00:00', '2017-03-02 00:00', '2016-11-22 00:01',))
if mibBuilder.loadTexts: vmwVRNIAgentCapabilityMIB.setLastUpdated('202005200000Z')
if mibBuilder.loadTexts: vmwVRNIAgentCapabilityMIB.setOrganization('VMware, Inc')
vmwVRNICapability = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 70, 125, 10))
vmwVRNIAgent2020v520 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 125, 10, 16))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVRNIAgent2020v520 = vmwVRNIAgent2020v520.setProductRelease('5.2.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVRNIAgent2020v520 = vmwVRNIAgent2020v520.setStatus('current')
vmwVRNIAgent2019v500 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 125, 10, 15))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVRNIAgent2019v500 = vmwVRNIAgent2019v500.setProductRelease('5.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVRNIAgent2019v500 = vmwVRNIAgent2019v500.setStatus('current')
vmwVRNIAgent2019v420 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 125, 10, 14))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVRNIAgent2019v420 = vmwVRNIAgent2019v420.setProductRelease('4.2.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVRNIAgent2019v420 = vmwVRNIAgent2019v420.setStatus('current')
vmwVRNIAgent2019v410 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 125, 10, 13))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVRNIAgent2019v410 = vmwVRNIAgent2019v410.setProductRelease('4.1.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVRNIAgent2019v410 = vmwVRNIAgent2019v410.setStatus('current')
vmwVRNIAgent2018v400 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 125, 10, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVRNIAgent2018v400 = vmwVRNIAgent2018v400.setProductRelease('4.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVRNIAgent2018v400 = vmwVRNIAgent2018v400.setStatus('current')
vmwVRNIAgent2018v390 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 125, 10, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVRNIAgent2018v390 = vmwVRNIAgent2018v390.setProductRelease('3.9.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVRNIAgent2018v390 = vmwVRNIAgent2018v390.setStatus('current')
vmwVRNIAgent2016v350 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 125, 10, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVRNIAgent2016v350 = vmwVRNIAgent2016v350.setProductRelease('3.5.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVRNIAgent2016v350 = vmwVRNIAgent2016v350.setStatus('current')
vmwVRNIAgent2017v340 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 125, 10, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVRNIAgent2017v340 = vmwVRNIAgent2017v340.setProductRelease('3.4.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVRNIAgent2017v340 = vmwVRNIAgent2017v340.setStatus('current')
vmwVRNIAgent2017v330 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 125, 10, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVRNIAgent2017v330 = vmwVRNIAgent2017v330.setProductRelease('3.3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVRNIAgent2017v330 = vmwVRNIAgent2017v330.setStatus('current')
vmwVRNIAgent2016v320 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 125, 10, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVRNIAgent2016v320 = vmwVRNIAgent2016v320.setProductRelease('3.2.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVRNIAgent2016v320 = vmwVRNIAgent2016v320.setStatus('current')
mibBuilder.exportSymbols("VMWARE-VRNI-AGENTCAP-MIB", vmwVRNIAgent2018v390=vmwVRNIAgent2018v390, vmwVRNIAgent2016v350=vmwVRNIAgent2016v350, vmwVRNIAgent2017v340=vmwVRNIAgent2017v340, vmwVRNIAgentCapabilityMIB=vmwVRNIAgentCapabilityMIB, PYSNMP_MODULE_ID=vmwVRNIAgentCapabilityMIB, vmwVRNIAgent2019v410=vmwVRNIAgent2019v410, vmwVRNICapability=vmwVRNICapability, vmwVRNIAgent2020v520=vmwVRNIAgent2020v520, vmwVRNIAgent2017v330=vmwVRNIAgent2017v330, vmwVRNIAgent2019v420=vmwVRNIAgent2019v420, vmwVRNIAgent2016v320=vmwVRNIAgent2016v320, vmwVRNIAgent2019v500=vmwVRNIAgent2019v500, vmwVRNIAgent2018v400=vmwVRNIAgent2018v400)
