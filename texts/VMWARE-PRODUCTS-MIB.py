#
# PySNMP MIB module VMWARE-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/vmware/VMWARE-PRODUCTS-MIB
# Produced by pysmi-1.1.10 at Fri Nov 10 13:29:06 2023
# On host fv-az1435-737 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, ObjectIdentity, Bits, Counter32, IpAddress, MibIdentifier, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Unsigned32, Counter64, iso, NotificationType, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "ObjectIdentity", "Bits", "Counter32", "IpAddress", "MibIdentifier", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Unsigned32", "Counter64", "iso", "NotificationType", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
vmwOID, vmwProductSpecific = mibBuilder.importSymbols("VMWARE-ROOT-MIB", "vmwOID", "vmwProductSpecific")
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
mibBuilder.exportSymbols("VMWARE-PRODUCTS-MIB", vmwDVS=vmwDVS, vmwEmbeddedVirtualCenterAppliance=vmwEmbeddedVirtualCenterAppliance, oidESX=oidESX, vmwNSXControllerAppliance=vmwNSXControllerAppliance, vmwVrops=vmwVrops, vmwManagementAppliance=vmwManagementAppliance, PYSNMP_MODULE_ID=vmwProducts, vmwInfrastructureAppliance=vmwInfrastructureAppliance, vmwVCOps=vmwVCOps, vmwNSX=vmwNSX, vmwESX=vmwESX, vmwNSXEdgeAppliance=vmwNSXEdgeAppliance, vmwGenericAppliance=vmwGenericAppliance, vmwProducts=vmwProducts, vmwHCXGateway=vmwHCXGateway, vmwVC=vmwVC, vmwHCXManager=vmwHCXManager, vmwServer=vmwServer, vmwNSXManagerAppliance=vmwNSXManagerAppliance)
