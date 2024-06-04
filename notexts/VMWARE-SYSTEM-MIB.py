#
# PySNMP MIB module VMWARE-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/vmware/VMWARE-SYSTEM-MIB
# Produced by pysmi-1.1.12 at Tue Jun  4 02:45:52 2024
# On host fv-az1200-411 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Counter32, TimeTicks, Gauge32, Unsigned32, NotificationType, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, IpAddress, Integer32, Bits, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "TimeTicks", "Gauge32", "Unsigned32", "NotificationType", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "IpAddress", "Integer32", "Bits", "ModuleIdentity")
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
mibBuilder.exportSymbols("VMWARE-SYSTEM-MIB", vmwProdPatch=vmwProdPatch, vmwSystemMIB=vmwSystemMIB, vmwSysMIBGroups=vmwSysMIBGroups, vmwSystemGroup=vmwSystemGroup, vmwProdVersion=vmwProdVersion, vmwProdBuild=vmwProdBuild, vmwProdName=vmwProdName, PYSNMP_MODULE_ID=vmwSystemMIB, vmwSystemMIBCompliances=vmwSystemMIBCompliances, vmwSystemMIBConformance=vmwSystemMIBConformance, vmwSysMIBBasicCompliance=vmwSysMIBBasicCompliance, vmwProdUpdate=vmwProdUpdate)
