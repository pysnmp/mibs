#
# PySNMP MIB module VMWARE-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/vmware/VMWARE-SYSTEM-MIB
# Produced by pysmi-1.1.10 at Thu Oct 26 12:39:24 2023
# On host fv-az583-292 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Integer32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter32, ObjectIdentity, Unsigned32, MibIdentifier, Gauge32, Bits, ModuleIdentity, iso, Counter64, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter32", "ObjectIdentity", "Unsigned32", "MibIdentifier", "Gauge32", "Bits", "ModuleIdentity", "iso", "Counter64", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
vmwSystem, = mibBuilder.importSymbols("VMWARE-ROOT-MIB", "vmwSystem")
vmwSystemMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6876, 1, 10))
vmwSystemMIB.setRevisions(('2010-08-02 00:00', '2008-01-12 00:00', '2007-12-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: vmwSystemMIB.setRevisionsDescriptions(('Add vmwProdPatch managed object to report patch level', 'Add to comments the Managed Object Browser (MOB) URLs which provide \n     data this MIB module exposes.', 'This is the first revision in SMIv2 format. One object\n    (vmwProdOID) has been dropped from the original SMIv1 version\n    as it duplicates sysObjectId from SNMPv2-MIB.',))
if mibBuilder.loadTexts: vmwSystemMIB.setLastUpdated('201008020000Z')
if mibBuilder.loadTexts: vmwSystemMIB.setOrganization('VMware, Inc')
if mibBuilder.loadTexts: vmwSystemMIB.setContactInfo('VMware, Inc\n    3401 Hillview Ave\n    Palo Alto, CA 94304\n    Tel: 1-877-486-9273 or 650-427-5000\n    Fax: 650-427-5001\n    Web: http://communities.vmware.com/community/developer/forums/managementapi\n    ')
if mibBuilder.loadTexts: vmwSystemMIB.setDescription('This MIB module provides for System Software identification')
vmwProdName = MibScalar((1, 3, 6, 1, 4, 1, 6876, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwProdName.setStatus('current')
if mibBuilder.loadTexts: vmwProdName.setDescription("This product's name.\n         VIM Property: AboutInfo.name\n         https://esx.example.com/mob/?moid=ServiceInstance&doPath=content%2eabout")
vmwProdVersion = MibScalar((1, 3, 6, 1, 4, 1, 6876, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwProdVersion.setStatus('current')
if mibBuilder.loadTexts: vmwProdVersion.setDescription("The product's version release identifier. Format is Major.Minor.Update\n         VIM Property: AboutInfo.version\n         https://esx.example.com/mob/?moid=ServiceInstance&doPath=content%2eabout")
vmwProdBuild = MibScalar((1, 3, 6, 1, 4, 1, 6876, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwProdBuild.setStatus('current')
if mibBuilder.loadTexts: vmwProdBuild.setDescription('This identifier represents the most specific identifier.\n         VIM Property: AboutInfo.build\n         https://esx.example.com/mob/?moid=ServiceInstance&doPath=content%2eabout')
vmwProdUpdate = MibScalar((1, 3, 6, 1, 4, 1, 6876, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwProdUpdate.setStatus('current')
if mibBuilder.loadTexts: vmwProdUpdate.setDescription('This identifier represents the update level applied to this system.\n         VIM Property: Advanced Options key: Misc.HostAgentUpdateLevel\n         https://esx.example.com/mob/?moid=ha%2dadv%2doptions')
vmwProdPatch = MibScalar((1, 3, 6, 1, 4, 1, 6876, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwProdPatch.setStatus('current')
if mibBuilder.loadTexts: vmwProdPatch.setDescription('This identifier represents the patch level applied to this system.\n         VIM Property: None. \n         CLI: esxcli system version get')
vmwSystemMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 1, 10, 2))
vmwSystemMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 1, 10, 2, 1))
vmwSysMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 1, 10, 2, 2))
vmwSysMIBBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6876, 1, 10, 2, 1, 2)).setObjects(("VMWARE-SYSTEM-MIB", "vmwSystemGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwSysMIBBasicCompliance = vmwSysMIBBasicCompliance.setStatus('current')
if mibBuilder.loadTexts: vmwSysMIBBasicCompliance.setDescription('The compliance statement for entities which implement the \n    VMWARE-SYSTEM-MIB.')
vmwSystemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6876, 1, 10, 2, 2, 1)).setObjects(("VMWARE-SYSTEM-MIB", "vmwProdName"), ("VMWARE-SYSTEM-MIB", "vmwProdVersion"), ("VMWARE-SYSTEM-MIB", "vmwProdBuild"), ("VMWARE-SYSTEM-MIB", "vmwProdUpdate"), ("VMWARE-SYSTEM-MIB", "vmwProdPatch"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwSystemGroup = vmwSystemGroup.setStatus('current')
if mibBuilder.loadTexts: vmwSystemGroup.setDescription('These objects uniquely identifies a given VMware system software image.')
mibBuilder.exportSymbols("VMWARE-SYSTEM-MIB", vmwSystemMIBConformance=vmwSystemMIBConformance, vmwProdVersion=vmwProdVersion, vmwSystemGroup=vmwSystemGroup, vmwSystemMIBCompliances=vmwSystemMIBCompliances, vmwSysMIBBasicCompliance=vmwSysMIBBasicCompliance, vmwProdPatch=vmwProdPatch, vmwProdName=vmwProdName, vmwProdBuild=vmwProdBuild, vmwSysMIBGroups=vmwSysMIBGroups, PYSNMP_MODULE_ID=vmwSystemMIB, vmwSystemMIB=vmwSystemMIB, vmwProdUpdate=vmwProdUpdate)
