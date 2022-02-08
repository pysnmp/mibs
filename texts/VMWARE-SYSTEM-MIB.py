#
# PySNMP MIB module VMWARE-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/vmware/VMWARE-SYSTEM-MIB
# Produced by pysmi-1.1.8 at Tue Feb  8 22:40:09 2022
# On host fv-az36-646 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ObjectIdentity, iso, TimeTicks, Gauge32, MibIdentifier, NotificationType, IpAddress, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Bits, ModuleIdentity, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "iso", "TimeTicks", "Gauge32", "MibIdentifier", "NotificationType", "IpAddress", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Bits", "ModuleIdentity", "Integer32", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("VMWARE-SYSTEM-MIB", PYSNMP_MODULE_ID=vmwSystemMIB, vmwProdPatch=vmwProdPatch, vmwProdVersion=vmwProdVersion, vmwProdUpdate=vmwProdUpdate, vmwSystemMIBConformance=vmwSystemMIBConformance, vmwSystemGroup=vmwSystemGroup, vmwSystemMIBCompliances=vmwSystemMIBCompliances, vmwSysMIBGroups=vmwSysMIBGroups, vmwSysMIBBasicCompliance=vmwSysMIBBasicCompliance, vmwProdBuild=vmwProdBuild, vmwSystemMIB=vmwSystemMIB, vmwProdName=vmwProdName)
