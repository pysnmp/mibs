#
# PySNMP MIB module VMWARE-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/vmware/VMWARE-PRODUCTS-MIB
# Produced by pysmi-1.1.12 at Tue Sep 17 10:06:22 2024
# On host fv-az1427-100 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.14 (main, Jul 16 2024, 19:03:10) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Integer32, MibIdentifier, ModuleIdentity, TimeTicks, iso, Unsigned32, Counter32, Gauge32, IpAddress, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Integer32", "MibIdentifier", "ModuleIdentity", "TimeTicks", "iso", "Unsigned32", "Counter32", "Gauge32", "IpAddress", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
vmwProductSpecific, vmwOID = mibBuilder.importSymbols("VMWARE-ROOT-MIB", "vmwProductSpecific", "vmwOID")
vmwProducts = ModuleIdentity((1, 3, 6, 1, 4, 1, 6876, 4, 11))
vmwProducts.setRevisions(('2018-06-27 00:00', '2017-10-13 00:00', '2017-05-17 00:00', '2015-07-17 00:00', '2014-09-19 00:00', '2011-09-29 00:00', '2007-07-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: vmwProducts.setRevisionsDescriptions(("Add vmwVrops snmp agent's sysObjectId value.", 'Changed vmwNSXManagerAppliance, vmwNSXManagerAppliance, and vmwNSXControllerAppliance oid.', 'Add vmwHCX appliance sysObjectIds.', 'Add vmwNSX', 'Add vSphere appliance sysObjectIds.', "Add vmwVCOps snmp agent's sysObjectId value.", 'The initial revision.',))
if mibBuilder.loadTexts: vmwProducts.setLastUpdated('201806270000Z')
if mibBuilder.loadTexts: vmwProducts.setOrganization('VMware, Inc')
if mibBuilder.loadTexts: vmwProducts.setContactInfo('VMware, Inc\n                3401 Hillview Ave\n                Palo Alto, CA 94304\n                Tel: 1-877-486-9273 or 650-427-5000\n                Fax: 650-427-5001\n                Web: http://kb.vmware.com/kb/1013445\n                ')
if mibBuilder.loadTexts: vmwProducts.setDescription('This MIB module provides the OID identifiers\n                which are returned from SNMPv2-MIB sysObjectId for\n                agents in specific VMware products.\n               ')
vmwESX = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 1))
vmwDVS = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 2))
vmwVC = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 3))
vmwServer = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 4))
vmwVCOps = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 5))
vmwVrops = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 50))
vmwGenericAppliance = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 6))
vmwEmbeddedVirtualCenterAppliance = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 7))
vmwInfrastructureAppliance = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 8))
vmwManagementAppliance = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 9))
vmwNSX = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 10))
vmwNSXEdgeAppliance = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 130))
vmwNSXManagerAppliance = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 131))
vmwNSXControllerAppliance = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 132))
vmwHCXManager = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 230))
vmwHCXGateway = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 31))
oidESX = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 60, 1))
mibBuilder.exportSymbols("VMWARE-PRODUCTS-MIB", vmwNSXControllerAppliance=vmwNSXControllerAppliance, vmwEmbeddedVirtualCenterAppliance=vmwEmbeddedVirtualCenterAppliance, vmwProducts=vmwProducts, vmwHCXManager=vmwHCXManager, vmwGenericAppliance=vmwGenericAppliance, vmwDVS=vmwDVS, vmwNSXManagerAppliance=vmwNSXManagerAppliance, PYSNMP_MODULE_ID=vmwProducts, vmwNSXEdgeAppliance=vmwNSXEdgeAppliance, vmwInfrastructureAppliance=vmwInfrastructureAppliance, vmwESX=vmwESX, vmwVCOps=vmwVCOps, vmwServer=vmwServer, oidESX=oidESX, vmwManagementAppliance=vmwManagementAppliance, vmwVC=vmwVC, vmwNSX=vmwNSX, vmwHCXGateway=vmwHCXGateway, vmwVrops=vmwVrops)
