#
# PySNMP MIB module VMWARE-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/vmware/VMWARE-SYSTEM-MIB
# Produced by pysmi-1.1.12 at Fri Nov 22 16:06:25 2024
# On host fv-az1245-338 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ModuleIdentity, Integer32, NotificationType, TimeTicks, ObjectIdentity, MibIdentifier, Bits, IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Gauge32, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "NotificationType", "TimeTicks", "ObjectIdentity", "MibIdentifier", "Bits", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Gauge32", "Counter64", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
vmwSystem, = mibBuilder.importSymbols("VMWARE-ROOT-MIB", "vmwSystem")
vmwSystemMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6876, 1, 10))
vmwSystemMIB.setRevisions(('2010-08-02 00:00', '2008-01-12 00:00', '2007-12-27 00:00',))
if mibBuilder.loadTexts: vmwSystemMIB.setLastUpdated('201008020000Z')
if mibBuilder.loadTexts: vmwSystemMIB.setOrganization('VMware, Inc')
vmwProdName = MibScalar((1, 3, 6, 1, 4, 1, 6876, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwProdName.setStatus('current')
vmwProdVersion = MibScalar((1, 3, 6, 1, 4, 1, 6876, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwProdVersion.setStatus('current')
vmwProdBuild = MibScalar((1, 3, 6, 1, 4, 1, 6876, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwProdBuild.setStatus('current')
vmwProdUpdate = MibScalar((1, 3, 6, 1, 4, 1, 6876, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwProdUpdate.setStatus('current')
vmwProdPatch = MibScalar((1, 3, 6, 1, 4, 1, 6876, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwProdPatch.setStatus('current')
vmwSystemMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 1, 10, 2))
vmwSystemMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 1, 10, 2, 1))
vmwSysMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 1, 10, 2, 2))
vmwSysMIBBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6876, 1, 10, 2, 1, 2)).setObjects(("VMWARE-SYSTEM-MIB", "vmwSystemGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwSysMIBBasicCompliance = vmwSysMIBBasicCompliance.setStatus('current')
vmwSystemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6876, 1, 10, 2, 2, 1)).setObjects(("VMWARE-SYSTEM-MIB", "vmwProdName"), ("VMWARE-SYSTEM-MIB", "vmwProdVersion"), ("VMWARE-SYSTEM-MIB", "vmwProdBuild"), ("VMWARE-SYSTEM-MIB", "vmwProdUpdate"), ("VMWARE-SYSTEM-MIB", "vmwProdPatch"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwSystemGroup = vmwSystemGroup.setStatus('current')
mibBuilder.exportSymbols("VMWARE-SYSTEM-MIB", vmwSystemMIBConformance=vmwSystemMIBConformance, vmwSysMIBGroups=vmwSysMIBGroups, vmwProdVersion=vmwProdVersion, vmwProdUpdate=vmwProdUpdate, PYSNMP_MODULE_ID=vmwSystemMIB, vmwProdPatch=vmwProdPatch, vmwSystemMIB=vmwSystemMIB, vmwSysMIBBasicCompliance=vmwSysMIBBasicCompliance, vmwProdBuild=vmwProdBuild, vmwSystemGroup=vmwSystemGroup, vmwSystemMIBCompliances=vmwSystemMIBCompliances, vmwProdName=vmwProdName)
