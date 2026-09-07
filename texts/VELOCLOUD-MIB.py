#
# PySNMP MIB module VELOCLOUD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source VELOCLOUD-MIB
# Source digest sha256:b2dad8f67221a979cf82a6237d5c9f4c623f2d0456e16a7f693936bc7e0dc5df
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, enterprises, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "enterprises", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
velocloud = ModuleIdentity((1, 3, 6, 1, 4, 1, 45346))
velocloud.setRevisions(('2021-05-11 00:00', '2019-08-02 00:00', '2017-01-18 00:00', '2017-01-13 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: velocloud.setRevisionsDescriptions(('Update of VMware nomenclature', 'Implementation of VMware SD-WAN Edge MIB Objects', 'Implementation of VCO MIB Objects', 'Inital definition of VMware SD-WAN MIB Objects',))
if mibBuilder.loadTexts: velocloud.setLastUpdated('2021-05-11 00:00')
if mibBuilder.loadTexts: velocloud.setOrganization('VMware Corporation')
if mibBuilder.loadTexts: velocloud.setContactInfo('postal:    VMware Corporation \n                                    World Headquarters\n                                    3401 Hillview Avenue\n                                    Palo Alto, CA 943043\n                                    USA\n                        \n                         web:       sase.vmware.com')
if mibBuilder.loadTexts: velocloud.setDescription('Top-level infrastructure of the VMware SD-WAN enterprise MIB tree')
modules = MibIdentifier((1, 3, 6, 1, 4, 1, 45346, 1))
mibBuilder.exportSymbols("VELOCLOUD-MIB", PYSNMP_MODULE_ID=velocloud, modules=modules, velocloud=velocloud)
