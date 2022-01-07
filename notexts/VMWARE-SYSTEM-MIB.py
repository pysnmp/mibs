#
# PySNMP MIB module VMWARE-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/vmware/VMWARE-SYSTEM-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:41:16 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, iso, Counter32, Integer32, TimeTicks, Counter64, ObjectIdentity, NotificationType, Unsigned32, Gauge32, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "iso", "Counter32", "Integer32", "TimeTicks", "Counter64", "ObjectIdentity", "NotificationType", "Unsigned32", "Gauge32", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("VMWARE-SYSTEM-MIB", vmwSystemMIBConformance=vmwSystemMIBConformance, PYSNMP_MODULE_ID=vmwSystemMIB, vmwProdVersion=vmwProdVersion, vmwSystemMIBCompliances=vmwSystemMIBCompliances, vmwProdName=vmwProdName, vmwProdPatch=vmwProdPatch, vmwSysMIBBasicCompliance=vmwSysMIBBasicCompliance, vmwSystemMIB=vmwSystemMIB, vmwProdBuild=vmwProdBuild, vmwSysMIBGroups=vmwSysMIBGroups, vmwSystemGroup=vmwSystemGroup, vmwProdUpdate=vmwProdUpdate)
